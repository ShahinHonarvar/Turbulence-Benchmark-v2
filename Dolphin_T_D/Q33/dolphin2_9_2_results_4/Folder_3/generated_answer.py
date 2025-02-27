def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(50, 77):
        if s[i] in vowels and s[i] > 'a' and (s[i] <= 'r'):
            result.append(s[i])
    return result