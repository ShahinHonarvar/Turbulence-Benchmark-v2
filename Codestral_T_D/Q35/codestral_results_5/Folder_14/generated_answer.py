def remove_repeat_chars(s):
    result = ''
    seen_chars = set()
    for i, char in enumerate(s):
        if 2 < i < 5:
            seen_chars.add(char)
        if char not in seen_chars or i <= 2 or i >= 5:
            result += char
    return result