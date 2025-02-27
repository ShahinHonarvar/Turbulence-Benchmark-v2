def remove_repeat_chars(text):
    seen = set()
    result = []
    for i, char in enumerate(text):
        if i < 30 or i >= 200:
            continue
        if char in seen:
            continue
        seen.add(char)
        result.append(char)
    return ''.join(result)