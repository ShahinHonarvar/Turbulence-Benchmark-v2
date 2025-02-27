def return_vowels(string):
    vowels = []
    for i in range(142, 145):
        if string[i].lower() == 'a' or string[i].lower() == 'e' or string[i].lower() == 'i' or (string[i].lower() == 'o') or (string[i].lower() == 'u'):
            if string[i] > '4' and string[i] <= 'o':
                vowels.append(string[i])
    return vowels