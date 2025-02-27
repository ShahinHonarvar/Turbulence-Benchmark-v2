def remove_repeat_chars(text):
    for char in text[86:99]:
        if text[86:99].count(char) > 1:
            text = text.replace(char, '')
    return text