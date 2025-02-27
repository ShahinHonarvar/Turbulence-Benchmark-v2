def return_vowels(string):
    vowels = []
    for i in range(60, 99):
        if i < len(string) and string[i] in 'aeiou' and (string[i] > 'j') and (string[i] <= 'n'):
            vowels.append(string[i])
    return vowels