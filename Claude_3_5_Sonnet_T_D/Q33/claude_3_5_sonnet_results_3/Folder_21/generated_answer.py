def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(464, 574):
        if i < len(s):
            if s[i].lower() in vowels and 'a' < s[i].lower() <= 'g':
                result.append(s[i])
    return result