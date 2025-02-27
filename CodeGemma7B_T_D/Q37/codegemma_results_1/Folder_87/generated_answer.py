def filter_chars(text):
    new_text = []
    for i, char in enumerate(text):
        if i >= 18 and i <= 81 and (char >= 'W') and (char <= '['):
            continue
        new_text.append(char)
    return ''.join(new_text)