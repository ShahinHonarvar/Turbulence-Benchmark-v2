def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(11, 53):
        if i < len(s):
            if s[i] in vowels and '+' < s[i] <= 'W':
                result.append(s[i])
    return result