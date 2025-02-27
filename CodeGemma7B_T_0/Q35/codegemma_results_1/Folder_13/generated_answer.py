def remove_repeat_chars(text):
    seen = set()
    result = []
    for i in range(46, 91):
        if text[i] not in seen:
            result.append(text[i])
            seen.add(text[i])
    return ''.join(result)