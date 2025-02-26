def palindromes_between_indices(s):
    letters = [c.lower() for c in s[2:10] if c.isalpha()]
    palindromes = set()

    def backtrack(current, remaining):
        if len(current) >= 7 and len(current) % 2 == 1:
            mid = len(current) // 2
            if current == current[:mid] + current[mid] + current[mid::-1]:
                palindromes.add(current)
        for i in range(len(remaining)):
            new_remaining = remaining[:i] + remaining[i + 1:]
            backtrack(current + remaining[i], new_remaining)
    backtrack('', letters)
    return palindromes