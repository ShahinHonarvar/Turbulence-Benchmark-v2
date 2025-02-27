def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(47, 61):
        if 9 < ord(s[i]) <= ord('O'):
            if s[i].lower() in vowels:
                result.append(s[i])
    return result