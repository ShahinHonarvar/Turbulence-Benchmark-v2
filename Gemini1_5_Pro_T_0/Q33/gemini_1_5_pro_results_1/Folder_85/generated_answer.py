def return_vowels(string):
    vowels = []
    for i in range(55, 65):
        if i < len(string) and string[i] in 'aeiouAEIOU' and (ord(string[i]) > ord('Z')) and (ord(string[i]) <= ord('w')):
            vowels.append(string[i])
    return vowels