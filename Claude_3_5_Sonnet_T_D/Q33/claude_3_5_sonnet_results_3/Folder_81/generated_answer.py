def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(20, 43):
        if i < len(s):
            if s[i] in vowels and '5' < s[i] <= 'M':
                result.append(s[i])
    return result