def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(133, 306):
        if i < len(s) and s[i] in vowels and (s[i] > 'c') and (s[i] <= 'd'):
            result.append(s[i])
    return result