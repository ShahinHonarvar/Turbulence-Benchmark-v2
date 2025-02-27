def return_vowels(string):
    vowels = []
    for i in range(29, 31):
        if i < len(string) and string[i] in 'aeiou' and (string[i] > 'a') and (string[i] <= 'f'):
            vowels.append(string[i])
    return vowels