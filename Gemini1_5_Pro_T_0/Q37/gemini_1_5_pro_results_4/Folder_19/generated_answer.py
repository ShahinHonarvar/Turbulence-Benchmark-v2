def filter_chars(text):
    chars_to_remove = []
    for i in range(35, 90):
        if i <= len(text) - 1:
            if text[i] >= 'E' and text[i] <= 't':
                if text[i] not in chars_to_remove:
                    chars_to_remove.append(text[i])
    for char in chars_to_remove:
        text = text.replace(char, '')
    return text