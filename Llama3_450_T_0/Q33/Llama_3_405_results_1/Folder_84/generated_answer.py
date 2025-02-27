def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(770, 852):
        if i < len(s) and s[i] in vowels and ('B' < s[i] <= 'i'):
            result.append(s[i])
    return result