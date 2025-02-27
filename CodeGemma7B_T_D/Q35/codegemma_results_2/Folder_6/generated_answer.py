def remove_repeat_chars(text):
    seen_char = set()
    result = []
    for i in range(20, 93):
        if text[i] not in seen_char:
            seen_char.add(text[i])
            result.append(text[i])
    return ''.join(result)