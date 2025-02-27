def filter_chars(text):
    for index in range(29, 80):
        if text[index] >= 'K' and text[index] <= 'z':
            for other_index in range(len(text)):
                if text[other_index] == text[index]:
                    text = text[:other_index] + text[other_index + 1:]
    return text