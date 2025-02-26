def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(142, 145):
        if i < len(s) and s[i] in vowels and ('4' < s[i] <= 'o'):
            result.append(s[i])
    return result