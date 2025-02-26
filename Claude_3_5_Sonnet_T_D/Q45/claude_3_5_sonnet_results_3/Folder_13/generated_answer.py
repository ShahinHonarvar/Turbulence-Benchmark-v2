def palindromes_between_indices(s):
    letters = ''.join((c.lower() for c in s[3:10] if c.isalpha()))
    n = len(letters)
    palindromes = set()

    def backtrack(current, remaining):
        if len(current) >= 5:
            if current == current[::-1]:
                palindromes.add(current)
        for i in range(len(remaining)):
            backtrack(current + remaining[i], remaining[:i] + remaining[i + 1:])
    backtrack('', letters)
    return palindromes