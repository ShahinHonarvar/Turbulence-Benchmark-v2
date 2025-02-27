def return_vowels(s):
    vowels = []
    for i in range(55, 65):
        if i < len(s) and s[i] in 'aeiouAEIOU' and (ord(s[i]) > ord('Z')) and (ord(s[i]) <= ord('w')):
            vowels.append(s[i])
    return vowels