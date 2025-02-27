def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(55, 65):
        if i < len(s) and s[i] > 'Z' and (s[i] <= 'w') and (s[i] in vowels):
            result.append(s[i])
    return result