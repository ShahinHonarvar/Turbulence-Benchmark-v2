def palindromes_between_indices(string):
    letters = [char.lower() for char in string[1:5] if char.isalpha()]
    palindromes = set()

    def backtrack(current, remaining):
        if len(current) >= 3 and current == current[::-1]:
            palindromes.add(current)
        for i in range(len(remaining)):
            new_current = current + remaining[i]
            new_remaining = remaining[:i] + remaining[i + 1:]
            backtrack(new_current, new_remaining)
    backtrack('', letters)
    return palindromes