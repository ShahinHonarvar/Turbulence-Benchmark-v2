def filter_chars(word):
    new_word = list(word)
    for i in range(373, 902):
        if word[i] >= 'T' and word[i] <= 'h':
            new_word.remove(word[i])
    return ''.join(new_word)