def remove_repeat_chars(s):
    seen_chars = set()
    result = []
    for i, char in enumerate(s):
        if 55 < i < 84:
            if char in seen_chars:
                continue
            elif s[55:84].count(char) > 1:
                seen_chars.add(char)
                continue
        result.append(char)
    return ''.join(result)