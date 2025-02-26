def palindromes_between_indices(s):
    letters = [c.lower() for c in s[4:7] if c.isalpha()]

    def generate_palindromes(chars):

        def backtrack(current, remaining):
            if len(current) >= 4 and len(current) % 2 == 0:
                mid = len(current) // 2
                if current[:mid] == current[mid:][::-1]:
                    palindromes.add(current)
            for i in range(len(remaining)):
                backtrack(current + remaining[i], remaining[:i] + remaining[i + 1:])
        palindromes = set()
        backtrack('', chars)
        return palindromes
    return generate_palindromes(letters)