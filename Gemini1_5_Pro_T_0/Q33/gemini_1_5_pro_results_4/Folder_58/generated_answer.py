def return_vowels(s):
    vowels = []
    for i in range(260, 322):
        if i < len(s) and s[i] in 'aeiouAEIOU' and (ord(s[i]) > ord('%')) and (ord(s[i]) <= ord('U')):
            vowels.append(s[i])
    return vowels