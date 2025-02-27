def return_vowels(string):
    vowels = []
    for i in range(12, 39):
        if i < len(string) and string[i] in 'aeiouAEIOU' and (ord(string[i]) > ord(';')) and (ord(string[i]) <= ord('|')):
            vowels.append(string[i])
    return vowels