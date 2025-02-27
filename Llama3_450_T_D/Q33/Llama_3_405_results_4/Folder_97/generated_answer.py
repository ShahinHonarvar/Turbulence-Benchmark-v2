def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(328, 455):
        if i < len(s) and s[i] in vowels and ('<' < s[i] <= 'z'):
            result.append(s[i])
    return result