def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(34, 58):
        if i < len(s):
            if s[i].lower() in vowels and 'b' < s[i].lower() <= 'o':
                result.append(s[i])
    return result