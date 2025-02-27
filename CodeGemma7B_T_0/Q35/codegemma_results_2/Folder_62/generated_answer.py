def remove_repeat_chars(text):
    seen = set()
    result = []
    for i, char in enumerate(text):
        if i < 50 or i >= 92:
            continue
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)