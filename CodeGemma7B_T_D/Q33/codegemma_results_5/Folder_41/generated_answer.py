def return_vowels(vowels):
    vowels_list = []
    for i in range(len(vowels)):
        if vowels[i] > '>' and vowels[i] <= 'U' and (i >= 71) and (i < 81):
            vowels_list.append(vowels[i])
    return vowels_list