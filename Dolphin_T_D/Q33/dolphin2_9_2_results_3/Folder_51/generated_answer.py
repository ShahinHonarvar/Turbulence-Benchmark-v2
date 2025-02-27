def return_vowels(string):
    vowels = ''
    for i in range(56, 68):
        if 'M' < string[i] <= 'X':
            vowels += string[i]
    return list(vowels)