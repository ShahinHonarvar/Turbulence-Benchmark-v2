def return_vowels(s):
    vowels = 'AEIOU'
    result = []
    for i in range(604, 949):
        if i < len(s):
            char = s[i].upper()
            if char in vowels and 'N' < char <= 'U':
                result.append(s[i])
    return result