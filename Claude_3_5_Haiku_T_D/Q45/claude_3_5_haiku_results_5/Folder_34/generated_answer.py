def palindromes_between_indices(s):
    letters = ''.join((c.lower() for c in s[5:8] if c.isalpha()))

    def generate_palindromes(chars):

        def backtrack(current, remaining):
            if len(current) >= 4 and len(current) % 2 == 0:
                if current == current[::-1]:
                    results.add(current)
            for i in range(len(remaining)):
                backtrack(current + remaining[i], remaining[:i] + remaining[i + 1:])
        results = set()
        backtrack('', chars)
        return results
    return generate_palindromes(letters)