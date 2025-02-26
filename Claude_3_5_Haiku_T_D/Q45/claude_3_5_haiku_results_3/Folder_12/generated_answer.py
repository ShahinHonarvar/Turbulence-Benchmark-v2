def palindromes_between_indices(s):
    letters = [char.lower() for char in s[3:9] if char.isalpha()]
    palindromes = set()

    def backtrack(current, remaining):
        if len(current) >= 4 and len(current) == 2 * (len(current) // 2):
            if current == current[::-1]:
                palindromes.add(current)
        for i in range(len(remaining)):
            backtrack(current + remaining[i], remaining[:i] + remaining[i + 1:])
    backtrack('', letters)
    return palindromes