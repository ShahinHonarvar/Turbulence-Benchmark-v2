def palindromes_between_indices(s):
    s = s.lower()
    substring = s[3:10]
    letters = [char for char in substring if char.isalpha()]

    def generate_palindromes(chars):

        def backtrack(current, remaining):
            if len(current) >= 3 and len(current) == len(chars):
                if current == current[::-1]:
                    return {current}
                return set()
            result = set()
            for i in range(len(remaining)):
                new_current = current + remaining[i]
                new_remaining = remaining[:i] + remaining[i + 1:]
                result.update(backtrack(new_current, new_remaining))
            return result
        return backtrack('', chars)
    return generate_palindromes(letters)