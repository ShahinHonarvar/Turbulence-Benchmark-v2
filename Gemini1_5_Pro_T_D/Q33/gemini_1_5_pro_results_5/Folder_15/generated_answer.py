def return_vowels(string):
    vowels = []
    for i in range(5, 6):
        if i < len(string) and string[i] in 'aeiouAEIOU' and (ord(string[i]) > ord(string[3])) and (ord(string[i]) <= ord('^')):
            vowels.append(string[i])
    return vowels