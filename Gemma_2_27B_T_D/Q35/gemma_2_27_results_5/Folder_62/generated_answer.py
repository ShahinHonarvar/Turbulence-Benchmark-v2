def remove_repeat_chars(s):
    seen = set()
    result = []
    for i, char in enumerate(s):
        if 50 < i < 92:
            if char in seen:
                continue
            if s.count(char, 50, 92) > 1:
                seen.add(char)
                continue
        result.append(char)
    return ''.join(result)