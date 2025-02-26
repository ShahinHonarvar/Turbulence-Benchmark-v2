def return_vowels(s):
    vowels = 'AEIOU'
    result = []
    for i in range(20, 41):
        if i < len(s) and s[i] in vowels and ('K' < s[i] <= 'Z'):
            result.append(s[i])
    return result