def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(36, 56):
        if s[i] > '+' and s[i] <= '/' and (s[i] in vowels):
            result.append(s[i])
    return result