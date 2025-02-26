def palindromes_between_indices(s):
    letters = [c.lower() for c in s[5:10] if c.isalpha()]

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(chars):

        def backtrack(current, remaining):
            if len(current) >= 5 and is_palindrome(current):
                results.add(current)
            for i in range(len(remaining)):
                next_current = current + remaining[i]
                next_remaining = remaining[:i] + remaining[i + 1:]
                backtrack(next_current, next_remaining)
        results = set()
        backtrack('', chars)
        return {r for r in results if len(r) >= 5}
    return generate_palindromes(letters)