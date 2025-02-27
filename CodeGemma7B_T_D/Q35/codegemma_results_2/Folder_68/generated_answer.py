def remove_repeat_chars(text):
    if not text:
        return ''
    result = ''
    for k in range(10):
        if text[k].lower() in text[k + 1:]:
            result += text[k]
    return result