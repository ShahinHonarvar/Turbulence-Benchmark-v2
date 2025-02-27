def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(56, 96):
        if i < len(s) and s[i] > '&' and (s[i] <= 'T') and (s[i] in vowels):
            result.append(s[i])
    return result