def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(27, 57):
        if i < len(s) and s[i] in vowels and ('o' < s[i] <= 'w'):
            result.append(s[i])
    return result