def return_vowels(string):
    vowels = []
    for i in range(8, 9):
        if i < len(string) and string[i] in 'aeiouAEIOU' and (ord(string[i]) > ord('Y')) and (ord(string[i]) <= ord('s')):
            vowels.append(string[i])
    return vowels