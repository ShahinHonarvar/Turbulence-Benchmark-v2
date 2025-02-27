def return_vowels(string):
    vowels = []
    for i in range(4, 8):
        if i < len(string) and 'P' < string[i] <= 'r' and (string[i] in 'aeiouAEIOU'):
            vowels.append(string[i])
    return vowels