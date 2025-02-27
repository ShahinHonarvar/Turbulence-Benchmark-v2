def return_vowels(string):
    vowels = []
    for i in range(1, 7):
        if i < len(string) and string[i] in 'aeiouAEIOU' and (string[i] > 'F') and (string[i] <= 'j'):
            vowels.append(string[i])
    return vowels