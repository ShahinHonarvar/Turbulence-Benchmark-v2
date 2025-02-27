def remove_repeat_chars(text):
    new_text = ''
    for i in range(len(text)):
        if i >= 476 and i <= 709:
            if text[i] not in new_text:
                new_text += text[i]
        else:
            new_text += text[i]
    return new_text