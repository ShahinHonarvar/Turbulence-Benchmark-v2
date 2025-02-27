def return_vowels(s):
    vowels = 'AEIO'
    result = []
    for i in range(37, 57):
        if i < len(s) and s[i] in vowels and ('*' < s[i] <= 'P'):
            result.append(s[i])
    return result