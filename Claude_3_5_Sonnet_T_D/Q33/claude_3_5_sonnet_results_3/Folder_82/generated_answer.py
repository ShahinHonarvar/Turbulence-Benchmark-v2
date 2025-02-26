def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(86, 99):
        if i < len(s):
            char = s[i].lower()
            if char in vowels and 'e' < char <= 'r':
                result.append(s[i])
    return result