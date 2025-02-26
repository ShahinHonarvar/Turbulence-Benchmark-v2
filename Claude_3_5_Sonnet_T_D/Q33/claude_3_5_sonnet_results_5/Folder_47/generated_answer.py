def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(23, 38):
        if i < len(s):
            char = s[i].lower()
            if char in vowels and 'n' < char <= 'k':
                result.append(s[i])
    return result