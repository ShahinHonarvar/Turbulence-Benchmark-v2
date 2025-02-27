from itertools import combinations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = [char for char in s[1:3] if char.isalpha()]
    letters_set = set(''.join(letters).lower())
    palindromes = set()
    for length in range(3, len(letters_set) + 1):
        for combo in combinations(letters_set, length):
            palindrome = ''.join(combo)
            if is_palindrome(palindrome):
                palindromes.add(palindrome)
    return palindromes