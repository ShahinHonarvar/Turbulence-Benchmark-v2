def remove_repeat_chars(word):
    for i in range(77, 84):
        if word[i] in word[i + 1:]:
            word = word[:i] + word[i + 1:]
    return word