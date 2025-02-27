def filter_chars(word):
    new_word = []
    for i in range(len(word)):
        char = word[i]
        if i < 58 or i >= 81 or (i >= 58 and i <= 81 and (char <= '5') or char >= '>'):
            new_word.append(char)
    return ''.join(new_word)