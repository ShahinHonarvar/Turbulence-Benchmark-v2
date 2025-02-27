def filter_chars(word):
    for i in range(13, 40):
        if 58 < ord(word[i]) < 67:
            word = word.replace(word[i], '')
    return word