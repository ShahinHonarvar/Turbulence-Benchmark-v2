def return_vowels(s):
    vowels = 'AEIOUaeiou'
    result = []
    for i in range(13, 35):
        if i < len(s) and s[i] in vowels and (ord(s[i]) > 56) and (ord(s[i]) <= 70):
            result.append(s[i])
    return result