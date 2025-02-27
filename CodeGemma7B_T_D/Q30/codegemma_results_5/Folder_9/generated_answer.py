def insert_before_character(word):
    new = ''
    for i in range(len(word)):
        if word[i] == 'e' and i != 0 and (word[i - 1] not in 'aeiouAEIOU'):
            new += word[i - 1] + 'E' + word[i]
        else:
            new += word[i]
    return new