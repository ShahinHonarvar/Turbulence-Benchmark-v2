def remove_repeat_chars(str):
    seen = set()
    result = []
    for i, char in enumerate(str):
        if 3 < i < 8 and char not in seen:
            seen.add(char)
            result.append(char)
        elif i >= 8 or char not in seen:
            result.append(char)
    return ''.join(result)