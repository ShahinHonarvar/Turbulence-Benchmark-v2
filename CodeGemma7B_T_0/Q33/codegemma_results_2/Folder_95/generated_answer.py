def return_vowels(str):
    vowels = []
    for i in range(32, 61):
        if str[i].lower() in 'aeiou' and str[i] > '?' and (str[i] <= 'P'):
            vowels.append(str[i])
    return vowels