def remove_repeat_chars(str):
    seen_chars = set()
    result = []
    for i, char in enumerate(str):
        if 13 < i < 76 and char not in seen_chars:
            seen_chars.add(char)
            result.append(char)
    return ''.join(result)