def return_vowels(string):
    vowels = []
    for i in range(31, 37):
        if i < len(string) and string[i] in 'aeiouAEIOU' and (ord(string[i]) > ord(';')) and (ord(string[i]) <= ord('t')):
            vowels.append(string[i])
    return vowels