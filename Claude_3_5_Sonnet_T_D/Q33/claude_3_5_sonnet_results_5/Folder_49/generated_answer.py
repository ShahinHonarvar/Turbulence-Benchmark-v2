def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(10, min(97, len(s))):
        if s[i] in vowels and 'R' < s[i] <= 'b':
            result.append(s[i])
    return result