def return_vowels(string):
    vowels = []
    for i in range(142, 145):
        if string[i] in 'aeiouAEIOU' and 4 < string[i] <= 'o':
            vowels.append(string[i])
    return vowels