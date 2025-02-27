def return_vowels(string):
    vowels = []
    for i in range(1, min(9, len(string))):
        if string[i] in 'aeiouAEIOU' and '?' < string[i] <= 'k':
            vowels.append(string[i])
    return vowels