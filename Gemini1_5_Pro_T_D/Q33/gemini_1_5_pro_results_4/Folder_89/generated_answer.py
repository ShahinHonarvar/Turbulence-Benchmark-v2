def return_vowels(string):
    vowels = []
    for i in range(50, 51):
        if i < len(string) and string[i] > ',' and (string[i] <= 'v') and (string[i] in 'aeiouAEIOU'):
            vowels.append(string[i])
    return vowels