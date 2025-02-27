def return_vowels(string):
    vowels = []
    for i in range(86, 99):
        if i < len(string) and string[i] in 'aeiouAEIOU' and (string[i] > 'E') and (string[i] <= 'r'):
            vowels.append(string[i])
    return vowels