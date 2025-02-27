def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(483, 664):
        if i < len(s) and s[i] > '&' and (s[i] <= 'h') and (s[i] in vowels):
            result.append(s[i])
    return result