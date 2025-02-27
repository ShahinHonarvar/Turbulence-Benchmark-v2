def return_vowels(s):
    vowels = []
    for i in range(71, 81):
        if i < len(s) and s[i] in 'AEIOUaeiou' and (ord(s[i]) > ord('>')) and (ord(s[i]) <= ord('U')):
            vowels.append(s[i])
    return vowels