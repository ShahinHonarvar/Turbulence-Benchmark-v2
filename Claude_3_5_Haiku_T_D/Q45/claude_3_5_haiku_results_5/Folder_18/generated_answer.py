def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:7] if c.isalpha()]

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(remaining_letters):
        palindromes = set()
        n = len(remaining_letters)
        for length in range(3, n + 1):
            for i in range(n):
                for perm in recursive_permutations(remaining_letters, length):
                    for p in perm:
                        if is_palindrome(p):
                            palindromes.add(p)
        return palindromes

    def recursive_permutations(letters, length):
        if length == 0:
            yield []
            return
        for i in range(len(letters)):
            current = letters[i]
            remaining = letters[:i] + letters[i + 1:]
            for p in recursive_permutations(remaining, length - 1):
                yield [current + ''.join(p)]
    return generate_palindromes(letters)