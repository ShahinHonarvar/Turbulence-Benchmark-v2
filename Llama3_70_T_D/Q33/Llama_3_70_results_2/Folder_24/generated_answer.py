def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(23, 57):
        if i < len(s) and s[i] != 0 and (s[i] <= 'd') and (s[i] in vowels):
            result.append(s[i])
    return result