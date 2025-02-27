def remove_repeat_chars(text):
    seen = set()
    result = []
    for i, char in enumerate(text):
        if i < 27 or i >= 96:
            continue
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)