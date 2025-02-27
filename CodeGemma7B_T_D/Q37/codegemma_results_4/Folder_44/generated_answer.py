def filter_chars(text):
    filtered_text = ''
    for char in text:
        if char.isalpha() and ord(char) >= ord('+') and (ord(char) <= ord('8')) and (text.index(char) >= 21) and (text.index(char) <= 43):
            continue
        else:
            filtered_text += char
    return filtered_text