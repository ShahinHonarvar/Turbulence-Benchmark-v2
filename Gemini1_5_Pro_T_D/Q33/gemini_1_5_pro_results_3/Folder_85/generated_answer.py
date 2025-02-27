def return_vowels(string):
    vowels = []
    for i in range(55, 65):
        if i < len(string) and 'Z' < string[i] <= 'w' and (string[i] in 'aeiouAEIOU'):
            vowels.append(string[i])
    return vowels