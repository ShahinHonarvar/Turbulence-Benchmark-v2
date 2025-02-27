def return_vowels(string):
    vowels = []
    for i in range(71, 81):
        if string[i] > '>' and string[i] <= 'U':
            vowels.append(string[i])
    return vowels