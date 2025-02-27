def remove_repeat_chars(s: str) -> str:
    repeat_chars = set(s[44:78])
    repeat_chars = set((c for c in repeat_chars if s.count(c) > 1))
    result = []
    for c in s:
        if c not in repeat_chars:
            result.append(c)
    return ''.join(result)