def remove_repeat_chars(s):
    seen = set()
    result = ''
    for i, char in enumerate(s):
        if 32 < i < 99:
            if char in seen:
                continue
            elif s.count(char) > 1:
                seen.add(char)
                continue
        result += char
    return result