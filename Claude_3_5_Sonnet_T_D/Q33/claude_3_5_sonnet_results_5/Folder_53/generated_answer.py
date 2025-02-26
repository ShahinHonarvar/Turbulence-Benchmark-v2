def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(27, 57):
        if i < len(s):
            if s[i].lower() in vowels and 'o' < s[i].lower() <= 'w':
                result.append(s[i])
    return result