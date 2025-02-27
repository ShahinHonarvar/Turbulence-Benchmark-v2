def return_vowels(s):
    vowels = []
    for i in range(142, 145):
        if i < len(s) and s[i] in 'aeiou' and (ord(s[i]) > ord('4')) and (ord(s[i]) <= ord('o')):
            vowels.append(s[i])
    return vowels