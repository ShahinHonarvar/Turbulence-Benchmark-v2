def return_vowels(s):
    vowels = []
    for i in range(43, 70):
        if i < len(s) and s[i] in 'aeiouAEIOU' and (ord(s[i]) > ord('*')) and (ord(s[i]) <= ord('b')):
            vowels.append(s[i])
    return vowels