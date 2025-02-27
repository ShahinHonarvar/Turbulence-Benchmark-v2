def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(63, 79):
        if 'D' < s[i] <= 'y' and s[i] in vowels:
            result.append(s[i])
    return result