def filter_chars(text):
    FILTER_RANGE = (227, 235)
    FILTER_CHAR_RANGE = ('D', 'u')
    filtered_text = ''
    for i, char in enumerate(text):
        if i not in range(*FILTER_RANGE) or char not in range(*FILTER_CHAR_RANGE):
            filtered_text += char
    return filtered_text