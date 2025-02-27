def remove_repeat_chars(s):
    seen_chars = set()
    result = []
    for i, char in enumerate(s):
        if 42 < i < 87 and char not in seen_chars:
            result.append(char)
            seen_chars.add(char)
    return ''.join(result)