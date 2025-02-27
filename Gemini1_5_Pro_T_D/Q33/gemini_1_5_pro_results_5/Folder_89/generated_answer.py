def return_vowels(string):
    vowels = []
    for i in range(50, 51):
        if i < len(string) and string[i] in 'aeiouAEIOU' and (ord(string[i]) > ord(',')) and (ord(string[i]) <= ord('v')):
            vowels.append(string[i])
    return vowels