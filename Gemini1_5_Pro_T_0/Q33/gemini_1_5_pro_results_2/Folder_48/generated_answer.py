def return_vowels(string):
    vowels = []
    for i in range(529, 828):
        if i < len(string) and string[i] in 'aeiouAEIOU' and (ord(string[i]) > ord('U')) and (ord(string[i]) <= ord('l')):
            vowels.append(string[i])
    return vowels