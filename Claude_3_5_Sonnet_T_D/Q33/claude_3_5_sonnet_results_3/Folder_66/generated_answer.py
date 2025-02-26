def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(63, 79):
        if i < len(s):
            if s[i] in vowels and 'D' < s[i] <= 'y':
                result.append(s[i])
    return result