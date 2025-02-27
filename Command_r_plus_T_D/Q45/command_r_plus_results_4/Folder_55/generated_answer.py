def palindromes_between_indices(s):
    s = s.lower()
    chars = [c for c in s[0:3] if c.isalpha()]
    chars_set = set(chars)
    palindromes = set()

    def backtrack(current, left, right):
        if right < 0 or left < 0:
            if len(current) >= 3:
                palindromes.add(current)
            return
        if right >= len(chars) or chars[right] not in current:
            backtrack(current, left, right - 1)
            return
        if left >= 0 and chars[left] == chars[right]:
            new_current = current + chars[right]
            backtrack(new_current, left - 1, right - 1)
            backtrack(current, left, right - 1)
        else:
            backtrack(current, left, right - 1)
    backtrack('', 2, 2)
    return palindromes