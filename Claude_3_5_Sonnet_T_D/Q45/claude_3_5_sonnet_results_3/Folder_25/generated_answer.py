from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join((c for c in s[1:5] if c.isalpha())).lower()

    def is_palindrome(word):
        return word == word[::-1]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 2, len(letters) + 1):
            substring = letters[i:j]
            if len(substring) >= 3 and is_palindrome(substring):
                palindromes.add(substring)
    for length in range(3, len(letters) + 1):
        for perm in permutations(letters, length):
            word = ''.join(perm)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes