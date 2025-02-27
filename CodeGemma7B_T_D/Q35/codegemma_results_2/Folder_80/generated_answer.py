def remove_repeat_chars(text):
    seen_chars = set()
    result = []
    for i in range(len(text)):
        if 57 < i < 84 and text[i] in seen_chars:
            continue
        seen_chars.add(text[i])
        result.append(text[i])
    return ''.join(result)