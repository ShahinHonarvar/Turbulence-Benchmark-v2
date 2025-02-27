def remove_repeat_chars(s):
    seen = set()
    result = []
    for i, char in enumerate(s):
        if i < 68 or i >= 100:
            continue
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)