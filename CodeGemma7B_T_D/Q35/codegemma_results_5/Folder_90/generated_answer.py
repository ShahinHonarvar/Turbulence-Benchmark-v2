def remove_repeat_chars(text):
    result = ''
    for i in range(len(text)):
        if i < 306 or i >= 807 or text[i] not in result:
            result += text[i]
    return result