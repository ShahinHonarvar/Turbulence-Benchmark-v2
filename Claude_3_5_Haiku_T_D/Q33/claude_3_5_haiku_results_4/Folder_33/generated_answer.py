def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(163, 771):
        if i < len(s) and s[i] in vowels and (':' < s[i] <= 'E'):
            result.append(s[i])
    return result