def filter_chars(text):
    filtered_text = ''
    for char in text:
        if ord(char) >= ord('-') and ord(char) <= ord('n') and (ord(char) < ord('A') or ord(char) > ord('z')):
            continue
        filtered_text += char
    return filtered_text