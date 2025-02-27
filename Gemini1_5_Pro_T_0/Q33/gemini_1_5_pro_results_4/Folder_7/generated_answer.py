def return_vowels(s):
    vowels = []
    for i in range(202, 872):
        if i < len(s) and s[i] in 'aeiouAEIOU' and (ord(s[i]) > ord('3')) and (ord(s[i]) <= ord('>')):
            vowels.append(s[i])
    return vowels