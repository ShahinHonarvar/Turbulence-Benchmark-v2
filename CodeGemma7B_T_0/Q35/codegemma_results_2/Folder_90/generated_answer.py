def remove_repeat_chars(text):
    seen = set()
    result = []
    for i in range(len(text)):
        if i < 306 or i >= 807:
            continue
        if text[i] not in seen:
            seen.add(text[i])
            result.append(text[i])
    return ''.join(result)