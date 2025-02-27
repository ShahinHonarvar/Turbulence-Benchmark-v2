def remove_repeat_chars(s):
    seen_chars = set()
    result = ''
    for i, char in enumerate(s):
        if 10 < i < 28:
            if char in seen_chars:
                continue
            else:
                seen_chars.add(char)
        result += char
    return result