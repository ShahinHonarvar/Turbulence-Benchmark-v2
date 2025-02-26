def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:8] if c.isalpha()]
    palindromes = set()

    def backtrack(current, remaining):
        if len(current) >= 6 and len(current) % 2 == 0:
            mid = len(current) // 2
            if current[:mid] == current[mid:][::-1]:
                palindromes.add(current)
        for i in range(len(remaining)):
            next_remaining = remaining[:i] + remaining[i + 1:]
            backtrack(current + remaining[i], next_remaining)
    backtrack('', letters)
    return palindromes