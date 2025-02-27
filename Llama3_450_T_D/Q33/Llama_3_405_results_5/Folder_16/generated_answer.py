def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(133, min(306, len(s))):
        if s[i] in vowels and 'c' < s[i] <= 'd':
            result.append(s[i])
    return result