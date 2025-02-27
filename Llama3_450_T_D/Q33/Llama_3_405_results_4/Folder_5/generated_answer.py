def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(44, 95):
        if i < len(s) and s[i] in vowels and (s[i] > chr(5)) and (s[i] <= '<'):
            result.append(s[i])
    return result