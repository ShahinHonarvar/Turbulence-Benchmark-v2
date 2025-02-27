def return_vowels(string):
    vowels = []
    for i in range(170, 645):
        if 'E' < string[i] <= '~':
            if string[i].lower() in {'a', 'e', 'i', 'o', 'u'}:
                vowels.append(string[i])
    return vowels