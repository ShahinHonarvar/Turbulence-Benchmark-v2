def return_vowels(string):
    vowels = []
    for i in range(528, 606):
        if string[i] in 'aeiouAEIOU' and string[i] > 'M' and (string[i] <= 'X'):
            vowels.append(string[i])
    return vowels