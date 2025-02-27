def return_vowels(string):
    vowels = []
    for i in range(1, 9):
        if string[i] in 'aeiouAEIOU' and string[i] > '?' and (string[i] <= 'k'):
            vowels.append(string[i])
    return vowels