def remove_repeat_chars(text):
    if not text:
        return text
    seen = set()
    result = []
    for i, char in enumerate(text):
        if 68 <= i < 99 and char in seen:
            continue
        seen.add(char)
        result.append(char)
    return ''.join(result)