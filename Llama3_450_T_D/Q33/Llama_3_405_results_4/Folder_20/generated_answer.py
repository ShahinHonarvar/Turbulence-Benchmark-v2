def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(59, 61):
        if i < len(s) and s[i] in vowels and ('+' < s[i] <= 'h'):
            result.append(s[i])
    return result