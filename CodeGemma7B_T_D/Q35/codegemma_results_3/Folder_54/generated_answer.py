def remove_repeat_chars(text):
    unique = []
    for i in range(35, 64):
        if text[i] not in unique:
            unique.append(text[i])
    result = ''
    for i in range(len(text)):
        if text[i] in unique:
            result += text[i]
    return result