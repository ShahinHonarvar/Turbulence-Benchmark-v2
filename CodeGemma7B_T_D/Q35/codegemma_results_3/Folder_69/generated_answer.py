def remove_repeat_chars(text):
    text = list(text)
    result = ''
    for i in range(39, 43):
        if text[i] in result:
            text[i] = ''
        else:
            result += text[i]
    return ''.join(text)