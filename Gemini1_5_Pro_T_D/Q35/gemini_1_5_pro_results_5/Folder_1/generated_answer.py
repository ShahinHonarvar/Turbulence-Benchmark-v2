def remove_repeat_chars(s):
    seen = set()
    result = ''
    for i, char in enumerate(s):
        if 17 < i < 88:
            if char in seen:
                continue
            else:
                seen.add(char)
        result += char
    return result