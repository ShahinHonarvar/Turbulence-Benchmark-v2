def remove_repeat_chars(string):
    seen_chars = set()
    result = []
    for i, char in enumerate(string):
        if 20 < i < 36:
            if char in seen_chars:
                continue
            else:
                seen_chars.add(char)
        result.append(char)
    return ''.join(result)