def palindromes_between_indices(s):
    low, high = (ord('a'), ord('z'))
    letters = [c for c in s[5:8] if low <= ord(c) <= high]
    if not letters:
        return set()
    results = set()

    def backtrack(pos):
        if pos >= len(letters):
            results.add(''.join(letters))
            return
        for i in range(pos, len(letters)):
            letters[pos], letters[i] = (letters[i], letters[pos])
            backtrack(pos + 1)
            letters[pos], letters[i] = (letters[i], letters[pos])
    backtrack(0)
    return results