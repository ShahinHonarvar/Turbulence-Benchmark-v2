def return_vowels(string):
    vowels = []
    for i in range(23, 85):
        if i < len(string) and 'W' < string[i] <= 'v' and (string[i] in 'aeiouAEIOU'):
            vowels.append(string[i])
    return vowels