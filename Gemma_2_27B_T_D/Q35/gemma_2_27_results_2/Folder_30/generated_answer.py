def remove_repeat_chars(text):
    seen = set()
    result = []
    for i in range(len(text)):
        if 22 < i < 24:
            if text[i] in seen:
                continue
            seen.add(text[i])
        result.append(text[i])
    return ''.join(result)