def filter_chars(text):
    for i in range(46, 68):
        temp = text[i]
        if temp > 'H' and temp < 's':
            text = text.replace(temp, '')
    return text