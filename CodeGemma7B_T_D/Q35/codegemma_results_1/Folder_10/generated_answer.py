def remove_repeat_chars(text):
    seen_chars = set()
    result = ''
    for i in range(36, 54):
        if text[i] not in seen_chars:
            seen_chars.add(text[i])
            result += text[i]
    return result