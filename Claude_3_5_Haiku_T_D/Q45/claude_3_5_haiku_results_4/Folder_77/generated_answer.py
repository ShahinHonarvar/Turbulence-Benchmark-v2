def palindromes_between_indices(s):
    letters = [c.lower() for c in s[4:7] if c.lower().isalpha()]
    palindromes = set()

    def backtrack(current_perm, remaining):
        if len(current_perm) == len(letters) * 2 and current_perm == current_perm[::-1]:
            palindromes.add(''.join(current_perm))
            return
        for i in range(len(remaining)):
            current_perm.append(remaining[i])
            backtrack(current_perm, remaining[:i] + remaining[i + 1:])
            current_perm.pop()
    if len(letters) >= 2:
        backtrack([], letters)
    return {p for p in palindromes if len(p) >= 4}