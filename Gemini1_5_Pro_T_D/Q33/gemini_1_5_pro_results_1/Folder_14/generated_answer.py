def return_vowels(string):
    vowels = []
    for i in range(47, 61):
        if i < len(string) and ord(string[i]) > 9 and (ord(string[i]) <= ord('O')) and (string[i] in 'aeiouAEIOU'):
            vowels.append(string[i])
    return vowels