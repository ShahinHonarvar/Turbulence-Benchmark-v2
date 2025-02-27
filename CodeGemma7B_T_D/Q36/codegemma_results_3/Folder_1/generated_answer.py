def filter_chars(word):
    filtered = ''
    for i in range(len(word)):
        if not (69 < i < 87 and word[i] > '#' and (word[i] < 'L')):
            filtered += word[i]
    return filtered