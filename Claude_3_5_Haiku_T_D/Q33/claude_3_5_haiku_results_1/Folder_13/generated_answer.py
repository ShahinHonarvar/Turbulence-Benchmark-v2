def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(149, 313):
        if i < len(s) and s[i] in vowels and (s[i] > 'M') and (s[i] <= 'j'):
            result.append(s[i])
    return result