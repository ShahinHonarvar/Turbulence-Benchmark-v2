def return_vowels(string):
    vowels = []
    for i in range(23, 75):
        if string[i] in 'aeiouAEIOU' and string[i] > 'L' and (string[i] <= 'd'):
            vowels.append(string[i])
    return vowels