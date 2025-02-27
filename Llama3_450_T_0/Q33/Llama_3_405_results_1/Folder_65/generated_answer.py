def return_vowels(s):
    vowels = 'AEIO'
    result = []
    for i in range(71, 88):
        if i < len(s) and s[i] in vowels and ('9' < s[i] <= 'P'):
            result.append(s[i])
    return result