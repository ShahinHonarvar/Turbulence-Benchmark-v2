def return_vowels(s):
    vowels = 'aeiou'
    result = []
    s = s[495:837]
    for i in range(len(s)):
        if s[i] > 'B' and s[i] <= 't' and (s[i] in vowels):
            result.append(s[i])
    return result