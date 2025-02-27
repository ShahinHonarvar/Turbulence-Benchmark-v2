def return_vowels(string):
    vowels = []
    for i in range(770, 852):
        if i < len(string) and string[i] in 'aeiouAEIOU' and (string[i] > 'B') and (string[i] <= 'i'):
            vowels.append(string[i])
    return vowels