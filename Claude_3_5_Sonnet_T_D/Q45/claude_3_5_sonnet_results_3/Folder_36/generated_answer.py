from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join((c.lower() for c in s[5:9] if c.isalpha()))

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(chars, length):
        if length <= 2:
            return set()
        result = set()
        for perm in permutations(chars, length):
            word = ''.join(perm)
            if is_palindrome(word):
                result.add(word)
        return result
    palindromes = set()
    for length in range(3, len(letters) + 1):
        palindromes.update(generate_palindromes(letters, length))
    return palindromes