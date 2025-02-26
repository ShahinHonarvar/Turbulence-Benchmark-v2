def palindromes_between_indices(s):
    letters = ''.join((c.lower() for c in s[1:8] if c.isalpha()))

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(chars, min_length):
        result = set()
        n = len(chars)
        for length in range(min_length, n + 1):
            for i in range(n - length + 1):
                substring = chars[i:i + length]
                permutations = set((''.join(p) for p in __import__('itertools').permutations(substring)))
                result.update((p for p in permutations if is_palindrome(p)))
        return result
    return generate_palindromes(letters, 5)