def return_vowels(str):
    vowels = []
    for i in range(1, 4):
        if str[i] > 'C' and str[i] <= 'I' and (str[i] in 'AEIOUaeiou'):
            vowels.append(str[i])
    return vowels