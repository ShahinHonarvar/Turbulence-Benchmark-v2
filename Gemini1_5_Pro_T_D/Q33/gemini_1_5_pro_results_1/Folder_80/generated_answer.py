def return_vowels(string):
    vowels = []
    for i in range(85, 99):
        if i < len(string) and string[i] in 'aeiouAEIOU' and ('/' < string[i] <= 'n'):
            vowels.append(string[i])
    return vowels