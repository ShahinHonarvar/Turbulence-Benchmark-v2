def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(837, 975):
        if i < len(s) and s[i] in vowels and ('N' < s[i] <= 'W'):
            result.append(s[i])
    return result