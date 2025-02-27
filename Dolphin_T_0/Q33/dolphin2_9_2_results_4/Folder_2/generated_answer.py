def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(170, 645):
        if 'E' < s[i] <= '~' and s[i] in vowels:
            result.append(s[i])
    return result