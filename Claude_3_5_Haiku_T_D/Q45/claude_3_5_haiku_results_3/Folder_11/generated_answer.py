def palindromes_between_indices(s):
    if len(s) < 8:
        return set()
    letters = [c.lower() for c in s[3:8] if c.isalpha()]
    if len(letters) < 4:
        return set()
    palindromes = set()

    def backtrack(current, remaining):
        if len(current) >= 4 and len(current) == len(remaining) * 2:
            palindrome = current + ''.join(reversed(current[:len(current) // 2]))
            palindromes.add(palindrome)
            return
        for i in range(len(remaining)):
            next_remaining = remaining[:i] + remaining[i + 1:]
            backtrack(current + remaining[i], next_remaining)
    backtrack('', letters)
    return palindromes