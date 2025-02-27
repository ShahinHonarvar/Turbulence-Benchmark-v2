def return_vowels(s):
    vowels = []
    for i in range(31, 37):
        if i < len(s) and s[i] in 'aeiouAEIOU' and (ord(s[i]) > ord(';')) and (ord(s[i]) <= ord('t')):
            vowels.append(s[i])
    return vowels