def remove_repeat_chars(s):
    seen = set()
    result = ''
    for i, char in enumerate(s):
        if 48 < i < 76:
            if char in seen:
                continue
            else:
                seen.add(char)
        result += char
    return result