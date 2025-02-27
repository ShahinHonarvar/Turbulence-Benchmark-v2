def remove_repeat_chars(s: str) -> str:
    repeat_chars = set(s[50:92])
    repeat_chars = set([c for c in repeat_chars if s.count(c) > 1])
    result = []
    for char in s:
        if char not in repeat_chars:
            result.append(char)
    return ''.join(result)