def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(86, 99):
        if i < len(s) and s[i] in vowels and ('E' < s[i] <= 'r'):
            result.append(s[i])
    return result