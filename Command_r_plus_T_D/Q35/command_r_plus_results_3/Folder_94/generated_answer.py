def remove_repeat_chars(s: str) -> str:
    repeat_chars = set(s[42:87])
    repeat_chars = set((char for char in repeat_chars if s.count(char) > 1))
    result = []
    for char in s:
        if char in repeat_chars:
            continue
        result.append(char)
    return ''.join(result)