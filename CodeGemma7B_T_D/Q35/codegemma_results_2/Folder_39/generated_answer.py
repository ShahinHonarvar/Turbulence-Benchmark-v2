def remove_repeat_chars(s):
    seen = set()
    result = []
    for i, char in enumerate(s):
        if 44 < i < 91 and char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)