def filter_chars(text):
    filtered_text = []
    for i in range(len(text)):
        if i < 57 or i >= 69 or text[i] <= '(' or (text[i] >= 'W'):
            filtered_text.append(text[i])
    return ''.join(filtered_text)