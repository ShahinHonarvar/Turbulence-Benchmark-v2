def remove_repeat_chars(s):
    seen = set()
    result = ''
    for i, char in enumerate(s):
        if 2 < i < 8:
            if char in seen:
                continue
            elif s[2:8].count(char) > 1:
                seen.add(char)
                continue
            else:
                result += char
        else:
            result += char
    return result