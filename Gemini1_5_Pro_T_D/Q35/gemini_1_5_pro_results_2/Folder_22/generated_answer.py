def remove_repeat_chars(s):
    seen_chars = set()
    result = []
    for i, char in enumerate(s):
        if 50 < i < 200:
            if char in seen_chars:
                continue
            else:
                seen_chars.add(char)
        result.append(char)
    return ''.join(result)