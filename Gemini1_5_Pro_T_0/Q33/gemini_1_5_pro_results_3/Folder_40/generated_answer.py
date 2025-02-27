def return_vowels(string):
    vowels = []
    for i in range(2, 7):
        if i < len(string) and string[i] in 'aeiouAEIOU' and ('^' < string[i] <= 'd'):
            vowels.append(string[i])
    return vowels