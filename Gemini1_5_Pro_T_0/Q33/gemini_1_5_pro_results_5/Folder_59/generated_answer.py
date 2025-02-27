def return_vowels(string):
    vowels = []
    for i in range(8, 9):
        if i < len(string) and string[i] > 'Y' and (string[i] <= 's') and (string[i] in 'aeiouAEIOU'):
            vowels.append(string[i])
    return vowels