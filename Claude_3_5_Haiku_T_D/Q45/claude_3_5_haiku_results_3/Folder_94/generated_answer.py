def palindromes_between_indices(s):
    if len(s) < 5:
        return set()
    letters = [c.lower() for c in s[3:5] if c.isalpha()]
    if len(letters) < 3:
        return set()

    def generate_palindromes(chars):

        def backtrack(path, remaining):
            if len(path) == len(chars):
                candidate = ''.join(path)
                if candidate == candidate[::-1]:
                    palindromes.add(candidate)
                return
            for i in range(len(remaining)):
                path.append(remaining[i])
                backtrack(path, remaining[:i] + remaining[i + 1:])
                path.pop()
        palindromes = set()
        backtrack([], chars)
        return {pal for pal in palindromes if len(pal) >= 3}
    return generate_palindromes(letters)