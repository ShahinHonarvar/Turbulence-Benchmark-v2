def remove_repeat_chars(s):
    if len(s) < 40:
        return ValueError('Input string is shorter than 40 characters.')
    seen = set()
    result = []
    for i, char in enumerate(s):
        if i < 20 or i >= 35 or char in seen:
            continue
        seen.add(char)
        result.append(char)
    return ''.join(result)