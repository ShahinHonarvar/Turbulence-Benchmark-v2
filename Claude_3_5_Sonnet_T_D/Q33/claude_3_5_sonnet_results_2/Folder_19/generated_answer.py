def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(51, 77):
        if i < len(s):
            if s[i] in vowels and '4' < s[i] <= '=':
                result.append(s[i])
    return result