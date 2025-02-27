def remove_repeat_chars(text):
    unique_chars = set()
    result = []
    for i in range(1, 7):
        if text[i] in unique_chars:
            continue
        unique_chars.add(text[i])
        result.append(text[i])
    return ''.join(result)