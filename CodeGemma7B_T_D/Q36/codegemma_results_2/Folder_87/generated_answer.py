def filter_chars(text):
    new_text = []
    for char in text:
        if char >= ' ' and char <= '!':
            if char not in new_text:
                new_text.append(char)
    return ''.join(new_text)