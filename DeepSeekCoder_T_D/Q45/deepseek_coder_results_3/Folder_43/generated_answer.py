from itertools import combinations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = ''.join(filter(str.isalpha, s[2:6].lower()))
    palindromes = set()
    for i in range(4, len(letters) + 1):
        for combo in combinations(letters, i):
            word = ''.join(combo)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes