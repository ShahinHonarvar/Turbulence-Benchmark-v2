def return_vowels(string):
    vowels = []
    for i in range(133, 306):
        if i < len(string) and string[i] in 'aeiouAEIOU' and (ord(string[i]) > ord('c')) and (ord(string[i]) <= ord('d')):
            vowels.append(string[i])
    return vowels