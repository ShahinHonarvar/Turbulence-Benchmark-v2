def filter_chars(text):
    result = ''
    for i in range(len(text)):
        if i < 41 or i >= 56 or (text[i] <= 'Z' and text[i] >= 'c'):
            continue
        result += text[i]
    return result