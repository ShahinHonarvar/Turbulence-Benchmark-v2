def return_vowels(s):
    vowels = 'AEIOUaeiou'
    result = []
    for i in range(170, 645):
        if i < len(s) and s[i] > 'E' and (s[i] <= '~') and (s[i] in vowels):
            result.append(s[i])
    return result