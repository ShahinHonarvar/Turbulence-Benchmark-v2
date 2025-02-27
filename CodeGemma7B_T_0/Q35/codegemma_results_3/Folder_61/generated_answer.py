def remove_repeat_chars(text):
    seen = set()
    result = []
    for char in text:
        if char in seen or char in text[:8]:
            continue
        seen.add(char)
        result.append(char)
    return ''.join(result)