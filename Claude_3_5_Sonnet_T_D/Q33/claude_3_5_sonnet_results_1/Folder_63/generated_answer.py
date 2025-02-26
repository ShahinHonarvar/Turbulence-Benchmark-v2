def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(34, 69):
        if i < len(s):
            char = s[i]
            if char.lower() in vowels and '_' < char <= 'o':
                result.append(char)
    return result