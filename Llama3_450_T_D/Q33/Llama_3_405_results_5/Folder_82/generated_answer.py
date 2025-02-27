def return_vowels(s):
    vowels = 'AEIOUaeiou'
    result = []
    for i in range(86, min(len(s), 99)):
        if s[i] > 'E' and s[i] <= 'r' and (s[i] in vowels):
            result.append(s[i])
    return result