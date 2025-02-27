def return_vowels(s):
    vowels = 'AEIOUaeiou'
    result = []
    for i in range(41, 50):
        if i < len(s) and s[i] > 'W' and (s[i] <= '[') and (s[i] in vowels):
            result.append(s[i])
    return result