def filter_chars(word):
    text = ''
    for i in range(len(word)):
        if i >= 75 and i <= 99 and (word[i] >= '8') and (word[i] <= 'e'):
            pass
        else:
            text += word[i]
    return text