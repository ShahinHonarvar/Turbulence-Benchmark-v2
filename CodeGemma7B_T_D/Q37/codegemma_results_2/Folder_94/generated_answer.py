def filter_chars(text):
    filtered_text = ''
    for i, char in enumerate(text):
        if 51 <= i <= 96 and ord(char) >= ord('X') and (ord(char) <= ord('p')):
            continue
        filtered_text += char
    return filtered_text