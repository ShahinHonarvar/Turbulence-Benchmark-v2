def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(604, 949):
        if i < len(s):
            char = s[i].lower()
            if char in vowels and 'n' < char <= 'u':
                result.append(s[i])
    return result