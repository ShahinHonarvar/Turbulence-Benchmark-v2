def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(604, 949):
        if i < len(s) and s[i] in vowels and ('N' < s[i] <= 'U'):
            result.append(s[i])
    return result