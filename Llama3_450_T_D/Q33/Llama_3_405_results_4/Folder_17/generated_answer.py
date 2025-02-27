def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(60, 99):
        if i < len(s) and s[i] > 'j' and (s[i] <= 'n') and (s[i] in vowels):
            result.append(s[i])
    return result