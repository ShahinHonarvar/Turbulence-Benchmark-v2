def filter_chars(text):
    result = ''
    for i in range(len(text)):
        if i < 43 or i >= 83 or text[i] <= ':' or (text[i] >= 'Q'):
            result += text[i]
    return result