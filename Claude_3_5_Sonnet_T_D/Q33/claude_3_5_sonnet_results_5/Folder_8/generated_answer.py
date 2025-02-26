def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(64, 82):
        if i < len(s):
            char = s[i]
            if char.lower() in vowels and 'P' < char <= 'z':
                result.append(char)
    return result