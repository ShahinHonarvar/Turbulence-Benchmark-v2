def return_vowels(string):
    vowels = []
    for i in range(2, 7):
        if i < len(string) and string[i] > '^' and (string[i] <= 'd') and (string[i] in 'aeiouAEIOU'):
            vowels.append(string[i])
    return vowels