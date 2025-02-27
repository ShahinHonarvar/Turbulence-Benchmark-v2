def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(70, 76):
        if i < len(s) and s[i] in vowels and (s[i] > '2') and (s[i] <= ':'):
            result.append(s[i])
    return result