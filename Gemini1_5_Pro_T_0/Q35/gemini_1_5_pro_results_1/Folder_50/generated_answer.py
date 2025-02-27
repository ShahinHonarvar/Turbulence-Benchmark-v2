def remove_repeat_chars(s):
    seen = set()
    result = ''
    for i, char in enumerate(s):
        if 13 < i < 76:
            if char in seen:
                continue
            elif s[14:76].count(char) > 1:
                seen.add(char)
                continue
        result += char
    return result