def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(44, 95):
        if i < len(s):
            if s[i] in vowels and '5' < s[i] <= '<':
                result.append(s[i])
    return result