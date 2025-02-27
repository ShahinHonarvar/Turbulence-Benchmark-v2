def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(46, 49):
        if i < len(s) and s[i] in vowels and ('[' < s[i] <= 'p'):
            result.append(s[i])
    return result