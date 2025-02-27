def return_vowels(string):
    vowels = []
    for i in range(21, 23):
        if i < len(string) and string[i] in 'aeiouAEIOU' and (string[i] > '-') and (string[i] <= 'n'):
            vowels.append(string[i])
    return vowels