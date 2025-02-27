def return_vowels(string):
    vowels = []
    for c in string[47:61]:
        if c > '9' and c <= 'O':
            vowels.append(c)
    return vowels