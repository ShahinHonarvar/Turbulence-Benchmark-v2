def remove_repeat_chars(s):
    seen = set()
    result = []
    for i, char in enumerate(s):
        if 90 <= i < 97 and char in seen:
            continue
        if 90 <= i < 97:
            seen.add(char)
        result.append(char)
    return ''.join(result)