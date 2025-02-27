def remove_repeat_chars(s):
    seen_chars = set()
    result = []
    for i, char in enumerate(s):
        if 49 < i < 74:
            if char in seen_chars:
                continue
            elif s[49:74].count(char) > 1:
                seen_chars.add(char)
                continue
        result.append(char)
    return ''.join(result)