def return_vowels(s):
    vowels = []
    for i in range(41, 50):
        if i < len(s) and s[i] in 'AEIOUaeiou' and (ord(s[i]) > ord('W')) and (ord(s[i]) <= ord('[')):
            vowels.append(s[i])
    return vowels