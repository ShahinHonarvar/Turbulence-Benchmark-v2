def remove_repeat_chars(text):
    for i in range(29, 53):
        letters[i] = letters[i] * dict.get(text[i], 0)
    return letters.join()