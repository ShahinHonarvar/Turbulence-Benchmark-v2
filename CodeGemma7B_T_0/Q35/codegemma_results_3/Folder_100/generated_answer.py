def remove_repeat_chars(text):
    seen = set()
    result = []
    for i in range(44, 78):
        if text[i] not in seen:
            seen.add(text[i])
            result.append(text[i])
    return ''.join(result)