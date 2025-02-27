def remove_repeat_chars(text):
    seen = set()
    result = []
    for i, char in enumerate(text):
        if char in seen or (i < 70 or i >= 200):
            continue
        seen.add(char)
        result.append(char)
    return ''.join(result)