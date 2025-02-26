def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(34, 69):
        if i < len(s):
            char = s[i].lower()
            if char in vowels and '_' < char <= 'o':
                result.append(s[i])
    return result