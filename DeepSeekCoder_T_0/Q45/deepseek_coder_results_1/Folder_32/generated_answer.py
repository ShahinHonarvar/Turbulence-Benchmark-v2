from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(letters):
        palindromes = set()
        for perm in permutations(letters, len(letters)):
            word = ''.join(perm)
            if is_palindrome(word):
                palindromes.add(word.lower())
        return palindromes
    letters = [char.lower() for char in s[1:8] if char.isalpha()]
    if len(letters) < 5:
        return set()
    all_palindromes = set()
    for i in range(5, len(letters) + 1):
        all_palindromes.update(generate_palindromes(letters[:i]))
    return all_palindromes