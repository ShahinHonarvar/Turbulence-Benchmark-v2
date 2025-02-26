def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(170, 645):
        if i < len(s):
            if s[i] in vowels and 'E' < s[i] <= '~':
                result.append(s[i])
    return result