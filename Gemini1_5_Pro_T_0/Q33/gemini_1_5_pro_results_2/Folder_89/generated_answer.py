def return_vowels(string):
    vowels = []
    for i in range(50, 51):
        if i < len(string) and string[i] in 'aeiouAEIOU' and (string[i] > ',') and (string[i] <= 'v'):
            vowels.append(string[i])
    return vowels