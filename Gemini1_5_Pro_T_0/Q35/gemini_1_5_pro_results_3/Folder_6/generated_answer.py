def remove_repeat_chars(s):
    seen_chars = set()
    result = ''
    for i, char in enumerate(s):
        if 20 < i < 93:
            if char in seen_chars:
                continue
            else:
                seen_chars.add(char)
        result += char
    return result