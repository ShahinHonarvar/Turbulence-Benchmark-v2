def remove_repeat_chars(text):
    seen = set()
    result = []
    for i in range(17, 88):
        if text[i] not in seen or i == 17:
            seen.add(text[i])
            result.append(text[i])
    return ''.join(result)