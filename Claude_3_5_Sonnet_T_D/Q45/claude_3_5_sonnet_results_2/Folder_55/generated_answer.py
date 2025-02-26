def palindromes_between_indices(s):
    letters = [c.lower() for c in s[:3] if c.isalpha()]
    result = set()

    def backtrack(current, remaining):
        if len(current) >= 3 and current == current[::-1]:
            result.add(current)
        for i in range(len(remaining)):
            backtrack(current + remaining[i], remaining[:i] + remaining[i + 1:])
    backtrack('', letters)
    return result