def palindromes_between_indices(s):
    letters = [char.lower() for char in s[:8] if char.isalpha()]

    def generate_palindromes(chars):

        def backtrack(current, remaining):
            if len(current) >= 4 and len(current) % 2 == 0:
                if current == current[::-1]:
                    palindromes.add(current)
            for i in range(len(remaining)):
                new_current = current + remaining[i]
                new_remaining = remaining[:i] + remaining[i + 1:]
                backtrack(new_current, new_remaining)
        palindromes = set()
        backtrack('', chars)
        return palindromes
    return generate_palindromes(letters)