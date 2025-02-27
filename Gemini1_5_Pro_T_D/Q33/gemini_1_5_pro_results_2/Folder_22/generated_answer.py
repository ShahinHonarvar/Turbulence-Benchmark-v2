def return_vowels(string):
    vowels = []
    for i in range(56, 90):
        if i < len(string) and string[i] in 'aeiouAEIOU' and (ord(string[i]) > ord('K')) and (ord(string[i]) <= ord('z')):
            vowels.append(string[i])
    return vowels