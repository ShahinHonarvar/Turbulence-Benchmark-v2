def return_vowels(string):
    vowels = []
    for i in range(19, 20):
        if i < len(string) and string[i] in 'aeiouAEIOU' and (string[i] > '<') and (string[i] <= 'p'):
            vowels.append(string[i])
    return vowels