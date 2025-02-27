def return_vowels(string):
    vowels = []
    for i in range(86, 99):
        if i < len(string) and string[i] in 'aeiouAEIOU' and (ord(string[i]) > ord('E')) and (ord(string[i]) <= ord('r')):
            vowels.append(string[i])
    return vowels