def return_vowels(s):
    vowels = 'AEIOU'
    result = []
    for i in range(19, 32):
        if 0 < s[i] <= 7:
            if s[i] in vowels:
                result.append(s[i])
    return result