def filter_chars(word):
    filtered = ''
    for i in range(len(word)):
        if i > 54 and i < 66 and (word[i] > 'f') and (word[i] < '|'):
            continue
        filtered += word[i]
    return filtered