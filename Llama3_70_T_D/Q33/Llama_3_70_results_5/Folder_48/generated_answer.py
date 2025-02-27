def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(529, min(828, len(s))):
        if s[i] in vowels and 'U' < s[i] <= 'l':
            result.append(s[i])
    return result