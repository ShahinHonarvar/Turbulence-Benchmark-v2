def return_vowels(s):
    vowels = []
    for i in range(19, 32):
        if i < len(s) and s[i] in 'aeiouAEIOU' and (ord(s[i]) > ord('0')) and (ord(s[i]) <= ord('7')):
            vowels.append(s[i])
    return vowels