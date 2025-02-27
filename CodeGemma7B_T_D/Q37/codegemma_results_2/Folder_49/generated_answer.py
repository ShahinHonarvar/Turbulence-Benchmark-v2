def filter_chars(text):
    filtered_text = ''
    for i in range(len(text)):
        if text[i] >= '*' and text[i] <= 'b' and (i >= 42) and (i <= 97):
            continue
        filtered_text += text[i]
    return filtered_text