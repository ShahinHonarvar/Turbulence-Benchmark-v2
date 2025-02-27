def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(24, 68):
        if i < len(s) and s[i] in vowels and ('f' < s[i] <= '|'):
            result.append(s[i])
    return result