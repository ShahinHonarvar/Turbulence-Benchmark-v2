def filter_chars(word):
    new_word = ''
    for i in range(len(word)):
        if i >= 10 and i <= 69 and (word[i] >= 'I') and (word[i] <= 'K'):
            pass
        else:
            new_word += word[i]
    return new_word