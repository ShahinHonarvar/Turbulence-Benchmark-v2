def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(528, 606):
        if i < len(s) and s[i] in vowels and ('M' < s[i] <= 'X'):
            result.append(s[i])
    return result