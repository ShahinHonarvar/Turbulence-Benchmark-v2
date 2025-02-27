def remove_repeat_chars(text):
    seen = set()
    result = []
    for i, char in enumerate(text):
        if i < 25 or i >= 80:
            continue
        if char in seen:
            continue
        seen.add(char)
        result.append(char)
    return ''.join(result)