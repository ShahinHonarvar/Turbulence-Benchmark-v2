def return_vowels(s):
    vowels = 'AEIOU'
    result = []
    for i in range(71, 81):
        if i < len(s) and s[i] in vowels and ('>' < s[i] <= 'U'):
            result.append(s[i])
    return result