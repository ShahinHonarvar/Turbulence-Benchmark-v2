def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(171, 402):
        if i < len(s) and s[i] > 'I' and (s[i] <= 'k') and (s[i] in vowels):
            result.append(s[i])
    return result