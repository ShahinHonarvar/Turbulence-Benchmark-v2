def remove_repeat_chars(s):
    seen_chars = set()
    result = []
    for i, char in enumerate(s):
        if 32 < i < 99 and s.count(char) > 1:
            if char not in seen_chars:
                seen_chars.add(char)
        else:
            result.append(char)
    return ''.join(result)