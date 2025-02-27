def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(21, 59):
        if i < len(s) and s[i] in vowels and ('/' < s[i] <= 'a'):
            result.append(s[i])
    return result