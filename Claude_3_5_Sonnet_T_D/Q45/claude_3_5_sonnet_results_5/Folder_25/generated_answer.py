from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[1:5])).lower()

    def is_palindrome(word):
        return word == word[::-1]
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for i in range(len(letters) - length + 1):
            substring = letters[i:i + length]
            if is_palindrome(substring):
                palindromes.add(substring)
    for perm_length in range(3, len(letters) + 1):
        for perm in permutations(letters, perm_length):
            word = ''.join(perm)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes