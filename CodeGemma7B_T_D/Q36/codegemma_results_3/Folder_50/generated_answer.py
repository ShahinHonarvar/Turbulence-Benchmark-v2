def filter_chars(text):
    for i in range(61, 88):
        for c in text:
            if i == ord(c) and c > '%' and (c < 'q'):
                text = text.replace(c, '')
    return text