def remove_repeat_chars(string):
    seen = set()
    result = []
    for i, char in enumerate(string):
        if i < 57 or i >= 85:
            continue
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)