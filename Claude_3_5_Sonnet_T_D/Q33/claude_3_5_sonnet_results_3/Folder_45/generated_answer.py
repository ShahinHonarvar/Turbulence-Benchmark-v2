def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(43, 70):
        if i < len(s):
            if s[i] in vowels and '*' < s[i] <= 'b':
                result.append(s[i])
    return result