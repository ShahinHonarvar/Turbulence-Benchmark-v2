def remove_repeat_chars(s):
    seen_chars = set()
    result = []
    for i, char in enumerate(s):
        if 103 < i < 802:
            if char in seen_chars:
                continue
            elif s.count(char, 104, 802) > 1:
                seen_chars.add(char)
                continue
        result.append(char)
    return ''.join(result)