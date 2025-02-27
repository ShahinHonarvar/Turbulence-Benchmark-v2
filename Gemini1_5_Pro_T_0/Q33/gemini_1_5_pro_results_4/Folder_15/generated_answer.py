def return_vowels(s):
    vowels = []
    for i in range(5, 6):
        if i < len(s) and ord(s[i]) > ord('3') and (ord(s[i]) <= ord('^')) and (s[i] in 'aeiouAEIOU'):
            vowels.append(s[i])
    return vowels