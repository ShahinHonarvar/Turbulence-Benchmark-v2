def filter_chars(text):
    filtered_text = []
    for i in range(len(text)):
        if 36 <= i <= 79 and text[i] in string.ascii_lowercase[1:18]:
            continue
        filtered_text.append(text[i])
    return ''.join(filtered_text)