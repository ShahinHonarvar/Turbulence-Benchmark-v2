def return_vowels(s):
    vowels = 'AEIOU'
    result = []
    for i in range(41, 50):
        if i < len(s) and s[i].upper() in vowels and (s[i] > 'W') and (s[i] <= '['):
            result.append(s[i])
    return result