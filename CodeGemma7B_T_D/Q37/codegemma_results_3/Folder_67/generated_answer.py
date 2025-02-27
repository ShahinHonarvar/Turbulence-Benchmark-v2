def filter_chars(text):
    filtered_text = []
    for i, char in enumerate(text):
        if i >= 19 and i <= 22 and (char >= ']') and (char <= 't'):
            pass
        else:
            filtered_text.append(char)
    return ''.join(filtered_text)