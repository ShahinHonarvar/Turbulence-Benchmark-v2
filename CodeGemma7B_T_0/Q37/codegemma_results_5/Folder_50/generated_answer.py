def filter_chars(text):
    for i in range(71, 97):
        if text[i] in string.ascii_letters and text[i] >= '_' and (text[i] <= 'o'):
            text = text[:i] + text[i + 1:]
    return text