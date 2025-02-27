def remove_repeat_chars(s):
    seen_chars = set()
    result = ''
    for i, char in enumerate(s):
        if 56 < i < 90:
            if char in seen_chars:
                continue
            elif s[56:90].count(char) > 1:
                seen_chars.add(char)
                continue
            else:
                result += char
            continue
        result += char
    return result