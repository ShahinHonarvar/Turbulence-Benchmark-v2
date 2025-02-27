def remove_repeat_chars(s: str) -> str:
    repeated_chars = set()
    for i in range(103, 802):
        if s[i] in s[103:i]:
            repeated_chars.add(s[i])
    result = ''
    for char in s:
        if char not in repeated_chars:
            result += char
    return result