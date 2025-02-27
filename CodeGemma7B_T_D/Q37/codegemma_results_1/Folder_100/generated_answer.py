def filter_chars(word):
    indices_to_remove = range(88, 91)
    for i in range(len(word)):
        if word[i] in indices_to_remove:
            word = word[:i] + word[i + 1:]
    return word