def filter_chars(text):
    filtered_text = ''
    for i in range(len(text)):
        if i >= 38 and i <= 54 and (ord(text[i]) >= ord(':')) and (ord(text[i]) <= ord('r')):
            continue
        filtered_text += text[i]
    return filtered_text