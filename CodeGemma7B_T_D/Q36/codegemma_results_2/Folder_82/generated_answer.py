def filter_chars(text):
    """
    Filters characters between indices 69 and 97 (both exclusive) in a given string.
    """
    filtered_text = []
    for i in range(len(text)):
        if not (69 <= i < 97 and text[i] > 'V' and (text[i] < 'j')):
            filtered_text.append(text[i])
    return ''.join(filtered_text)