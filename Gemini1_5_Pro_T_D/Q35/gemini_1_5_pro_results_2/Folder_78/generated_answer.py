def remove_repeat_chars(s):
    seen_chars = set()
    result = []
    for i, char in enumerate(s):
        if 62 < i < 96 and s.count(char) > 1:
            if char in seen_chars:
                continue
            else:
                seen_chars.add(char)
        result.append(char)
    return ''.join(result)