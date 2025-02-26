def palindromes_between_indices(s):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    letters = ''.join(filter(lambda x: x.lower() in alphabet, s[1:8])).lower()

    def is_palindrome(word):
        return word == word[::-1]
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for i in range(len(letters) - length + 1):
            substring = letters[i:i + length]
            perms = set((''.join(p) for p in __import__('itertools').permutations(substring)))
            palindromes.update(filter(is_palindrome, perms))
    return palindromes