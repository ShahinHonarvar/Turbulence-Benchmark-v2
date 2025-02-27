def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(85, min(len(s), 99)):
        if s[i] > '/' and s[i] <= 'n' and (s[i] in vowels):
            result.append(s[i])
    return result