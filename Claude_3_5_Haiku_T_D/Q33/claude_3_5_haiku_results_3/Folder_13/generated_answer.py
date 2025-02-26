def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(149, 313):
        if i < len(s) and s[i] in vowels and ('M' < s[i] <= 'j'):
            result.append(s[i])
    return result