def palindromes_between_indices(s):
    letters = ''.join((c.lower() for c in s[:7] if c.isalpha()))

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(chars, min_length):
        result = set()
        n = len(chars)

        def backtrack(current, remaining):
            if len(current) >= min_length and is_palindrome(current):
                result.add(current)
            for i in range(len(remaining)):
                backtrack(current + remaining[i], remaining[:i] + remaining[i + 1:])
        backtrack('', chars)
        return result
    return generate_palindromes(letters, 5)