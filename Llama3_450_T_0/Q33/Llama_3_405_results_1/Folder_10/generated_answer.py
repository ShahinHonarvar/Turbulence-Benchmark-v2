def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(31, 37):
        if i < len(s) and s[i] in vowels and (';' < s[i] <= 't'):
            result.append(s[i])
    return result