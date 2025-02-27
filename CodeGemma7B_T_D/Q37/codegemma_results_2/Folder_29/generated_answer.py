def filter_chars(text):
    filtered_text = ''
    for i in range(len(text)):
        if i >= 12 and i <= 88 and (ord(text[i]) >= ord('&')) and (ord(text[i]) <= ord('v')):
            continue
        filtered_text += text[i]
    return filtered_text