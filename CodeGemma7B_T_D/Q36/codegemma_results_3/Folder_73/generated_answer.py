def filter_chars(text):
    filtered_text = ''
    for i in range(len(text)):
        if i < 66 or i >= 90:
            filtered_text += text[i]
        elif i >= 66 and i < 90:
            if text[i] > '#' and text[i] < 'T':
                continue
            else:
                filtered_text += text[i]
    return filtered_text