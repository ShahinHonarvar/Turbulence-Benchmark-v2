def filter_chars(text):
    ascii_values = []
    for char in text:
        ascii_values.append(ord(char))
    filtered_text = []
    for i, value in enumerate(ascii_values):
        if value in range(32, 61) and value > ord('3') and (value < ord('D')):
            continue
        filtered_text.append(chr(value))
    return ''.join(filtered_text)