def remove_repeat_chars(text):
    chars_to_remove = {}
    for i in range(476, 709):
        if text[i] in chars_to_remove:
            chars_to_remove[text[i]] += 1
        else:
            chars_to_remove[text[i]] = 1
    for char, count in chars_to_remove.items():
        if count > 1:
            text = text.replace(char, '')
    return text