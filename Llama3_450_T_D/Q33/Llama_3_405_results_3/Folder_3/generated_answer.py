def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(50, 77):
        if i < len(s) and s[i] > '#' and (s[i] <= 'r') and (s[i] in vowels):
            result.append(s[i])
    return result