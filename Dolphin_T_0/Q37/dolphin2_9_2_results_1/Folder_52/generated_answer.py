def filter_chars(text):
    for i in range(54, 84):
        if 'j' <= text[i] <= 'v':
            copy = ''
            for j in range(len(text)):
                if text[j] != text[i]:
                    copy = copy + text[j]
            text = copy
    return text