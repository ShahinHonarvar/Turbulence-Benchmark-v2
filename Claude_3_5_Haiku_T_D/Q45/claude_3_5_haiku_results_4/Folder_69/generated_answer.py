def palindromes_between_indices(s):
    letters = [char.lower() for char in s[:4] if char.isalpha()]

    def generate_palindromes(letters):

        def backtrack(current, remaining):
            if len(current) >= 4 and len(current) % 2 == 0:
                if current == current[::-1]:
                    result.add(current)
            for i in range(len(remaining)):
                backtrack(current + remaining[i], remaining[:i] + remaining[i + 1:])
        result = set()
        backtrack('', letters)
        return result
    return generate_palindromes(letters)