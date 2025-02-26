def palindromes_between_indices(s):
    s = s.lower()
    substring = s[2:7]
    letters = [char for char in substring if char.isalpha()]

    def generate_palindromes(chars):

        def backtrack(current, remaining):
            if len(current) >= 3 and len(current) % 2 == 1:
                if current == current[::-1]:
                    result.add(current)
            for i in range(len(remaining)):
                backtrack(current + remaining[i], remaining[:i] + remaining[i + 1:])
        result = set()
        backtrack('', chars)
        return result
    return generate_palindromes(letters)