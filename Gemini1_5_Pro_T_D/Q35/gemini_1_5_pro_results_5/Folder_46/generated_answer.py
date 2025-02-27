def remove_repeat_chars(s):
    seen = set()
    result = ''
    for i, char in enumerate(s):
        if 10 < i < 79:
            if char in seen:
                continue
            elif s[10:79].count(char) > 1:
                seen.add(char)
                continue
        result += char
    return result