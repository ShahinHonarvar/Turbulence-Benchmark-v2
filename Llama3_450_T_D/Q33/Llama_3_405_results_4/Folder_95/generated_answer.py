def return_vowels(s):
    vowels = 'AEIO'
    result = []
    for i in range(32, 61):
        if i < len(s) and s[i] in vowels and ('?' < s[i] <= 'P'):
            result.append(s[i])
    return result