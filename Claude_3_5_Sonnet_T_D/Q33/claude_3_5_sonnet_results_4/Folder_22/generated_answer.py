def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(56, 90):
        if i < len(s):
            if s[i] in vowels and 'K' < s[i] <= 'z':
                result.append(s[i])
    return result