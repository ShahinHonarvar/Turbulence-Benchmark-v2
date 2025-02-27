def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(171, 402):
        if i < len(s) and s[i] in vowels and ('I' < s[i] <= 'k'):
            result.append(s[i])
    return result