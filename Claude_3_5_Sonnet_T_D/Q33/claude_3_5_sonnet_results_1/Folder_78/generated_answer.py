def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(46, 90):
        if i < len(s):
            if s[i] in vowels and '@' < s[i] <= '[':
                result.append(s[i])
    return result