def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(17, 65):
        if i < len(s) and s[i] in vowels and ('U' < s[i] <= '{'):
            result.append(s[i])
    return result