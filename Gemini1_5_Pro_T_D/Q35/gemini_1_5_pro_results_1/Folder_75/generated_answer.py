def remove_repeat_chars(s):
    seen = set()
    result = ''
    for i, char in enumerate(s):
        if 20 < i < 51:
            if char in seen:
                continue
            elif s[21:51].count(char) > 1:
                seen.add(char)
                continue
        result += char
    return result