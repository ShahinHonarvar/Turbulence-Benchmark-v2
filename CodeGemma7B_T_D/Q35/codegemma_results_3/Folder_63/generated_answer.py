def remove_repeat_chars(word):
    for i in range(81, 86):
        for k in range(i + 1, 86):
            if word[i] == word[k]:
                word = word[:i] + word[i + 1:]
                break
    return word