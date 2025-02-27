def filter_chars(text):
    filtered_text = ''
    for char in text:
        if char >= '?' and char <= 'f' and (text.index(char) in range(2, 7)):
            continue
        filtered_text += char
    return filtered_text