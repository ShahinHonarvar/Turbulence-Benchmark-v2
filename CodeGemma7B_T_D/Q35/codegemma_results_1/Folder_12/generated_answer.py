def remove_repeat_chars(text):
    chars = set()
    result = ''
    for i in range(16, 87):
        if text[i] not in chars:
            result += text[i]
            chars.add(text[i])
    return result