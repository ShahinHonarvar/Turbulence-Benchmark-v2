def remove_repeat_chars(s):
    seen_chars = set()
    result = []
    for i, char in enumerate(s):
        if 27 < i < 96:
            if char in seen_chars:
                continue
            elif s.count(char) > 1:
                seen_chars.add(char)
                continue
        result.append(char)
    return ''.join(result)