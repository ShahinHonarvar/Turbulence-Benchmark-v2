def palindromes_between_indices(s):
    letters = [char.lower() for char in s[4:9] if char.isalpha()]
    results = set()

    def backtrack(current, remaining):
        if len(current) >= 5 and len(current) % 2 == 1:
            if current == current[::-1]:
                results.add(current)
        for i in range(len(remaining)):
            backtrack(current + remaining[i], remaining[:i] + remaining[i + 1:])
    backtrack('', letters)
    return results