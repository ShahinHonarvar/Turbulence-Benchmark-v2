def remove_repeat_chars(string):
    seen = set()
    result = []
    for i, char in enumerate(string):
        if not 56 < i < 90:
            continue
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)