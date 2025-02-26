def palindromes_between_indices(s):
    letters = [char.lower() for char in s[4:9] if char.isalpha()]
    palindromes = set()

    def backtrack(current, remaining):
        if len(current) >= 4 and len(current) % 2 == 0:
            if current == current[::-1]:
                palindromes.add(current)
        for i in range(len(remaining)):
            new_current = current + remaining[i]
            new_remaining = remaining[:i] + remaining[i + 1:]
            backtrack(new_current, new_remaining)
    backtrack('', letters)
    return palindromes