def remove_repeat_chars(s):
    result = []
    seen = set()
    for i, char in enumerate(s):
        if 11 <= i < 76 and char in seen:
            continue
        seen.add(char)
        if 11 <= i < 76:
            seen.discard(char)
        result.append(char)
    return ''.join(result)