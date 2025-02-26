def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(55, 65):
        if i < len(s):
            if s[i].lower() in vowels and 'Z' < s[i] <= 'w':
                result.append(s[i])
    return result