def remove_repeat_chars(s):
    seen = set()
    result = ''
    for i, char in enumerate(s):
        if 2 < i < 5:
            if char in seen:
                continue
            else:
                seen.add(char)
        if char not in seen:
            result += char
    return result