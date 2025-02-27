def filter_chars(text):
    filtered_text = ''
    for i, char in enumerate(text):
        if i in range(35, 99) and ord(char) in range(ord('A'), ord('b') + 1):
            continue
        filtered_text += char
    return filtered_text