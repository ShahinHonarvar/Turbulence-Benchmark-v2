def filter_chars(word):
    new_word = ''
    for i in range(len(word)):
        if word[i] in "789:;<=>?@[\\]^_`{'|}":
            continue
        new_word += word[i]
    return new_word