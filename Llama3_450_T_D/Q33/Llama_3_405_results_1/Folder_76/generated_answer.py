def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(495, 837):
        if i < len(s) and s[i] > 'B' and (s[i] <= 't') and (s[i] in vowels):
            result.append(s[i])
    return result