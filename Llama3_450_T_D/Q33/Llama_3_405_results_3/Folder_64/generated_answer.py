def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(1, 7):
        if i < len(s) and s[i] in vowels and ('F' < s[i] <= 'j'):
            result.append(s[i])
    return result