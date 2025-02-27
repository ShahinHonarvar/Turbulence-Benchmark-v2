def remove_repeat_chars(word):
    unique_chars = set()
    for i in range(7, 9):
        if word[i] not in unique_chars:
            unique_chars.add(word[i])
        else:
            word = word.replace(word[i], '')
    return word