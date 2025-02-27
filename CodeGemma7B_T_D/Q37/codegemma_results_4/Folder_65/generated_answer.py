def filter_chars(text):
    for i in range(61, 71):
        for j in text:
            if j == chr(i):
                text = text.replace(j, '')
    return text