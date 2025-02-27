def remove_repeat_chars(s):
    seen_chars = set()
    result = ''
    for i, char in enumerate(s):
        if 38 < i < 81:
            if char in seen_chars:
                continue
            elif s[38:81].count(char) > 1:
                seen_chars.add(char)
                continue
        result += char
    return result