def remove_repeat_chars(s):
    seen_chars = set()
    result = []
    for i, char in enumerate(s):
        if 10 < i < 76:
            if char in seen_chars:
                continue
            elif s[10:76].count(char) > 1:
                seen_chars.add(char)
                continue
        result.append(char)
    return ''.join(result)