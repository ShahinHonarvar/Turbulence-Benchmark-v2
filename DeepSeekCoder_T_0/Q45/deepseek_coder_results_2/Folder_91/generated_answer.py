from itertools import combinations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = set(s[2:7].lower())
    palindromes = set()
    for i in range(3, len(letters) + 1):
        for combo in combinations(letters, i):
            word = ''.join(combo)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes