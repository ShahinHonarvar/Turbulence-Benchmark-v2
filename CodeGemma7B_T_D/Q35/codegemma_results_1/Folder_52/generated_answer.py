def remove_repeat_chars(s):
    seen_chars = set()
    result = []
    for i, char in enumerate(s):
        if 38 < i < 81 and char in seen_chars:
            continue
        seen_chars.add(char)
        result.append(char)
    return ''.join(result)