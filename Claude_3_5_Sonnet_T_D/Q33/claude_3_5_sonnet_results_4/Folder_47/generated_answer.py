def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(23, 38):
        if i < len(s):
            if s[i].lower() in vowels and 'N' < s[i] <= 'k':
                result.append(s[i])
    return result