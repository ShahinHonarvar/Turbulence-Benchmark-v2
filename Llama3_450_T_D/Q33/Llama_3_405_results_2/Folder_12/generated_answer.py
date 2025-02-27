def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(13, 37):
        if i < len(s) and s[i] in vowels and ('Z' < s[i] <= '}'):
            result.append(s[i])
    return result