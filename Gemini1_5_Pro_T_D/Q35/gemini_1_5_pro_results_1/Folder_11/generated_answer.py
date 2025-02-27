def remove_repeat_chars(s):
    seen = set()
    result = ''
    for i, char in enumerate(s):
        if 48 < i < 76 and s.count(char) > 1:
            if char not in seen:
                seen.add(char)
                result += char
        else:
            result += char
    return result