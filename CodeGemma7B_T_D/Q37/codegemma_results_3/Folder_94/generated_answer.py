def filter_chars(text):
    filtered_text = ''
    for i in range(len(text)):
        if i in range(51, 97) and ord(text[i]) in range(ord('X'), ord('p') + 1):
            continue
        filtered_text += text[i]
    return filtered_text