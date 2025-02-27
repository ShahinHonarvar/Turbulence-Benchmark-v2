def return_vowels(string):
    vowels = []
    for i in range(163, 771):
        if i < len(string) and string[i] in 'aeiouAEIOU' and (string[i] > ':') and (string[i] <= 'E'):
            vowels.append(string[i])
    return vowels