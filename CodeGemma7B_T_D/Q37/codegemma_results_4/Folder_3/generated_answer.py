def filter_chars(word):
    new_word = ''
    for i, c in enumerate(word):
        if i >= 37 and i <= 56 and (c >= '6') and (c <= '_'):
            continue
        new_word += c
    return new_word