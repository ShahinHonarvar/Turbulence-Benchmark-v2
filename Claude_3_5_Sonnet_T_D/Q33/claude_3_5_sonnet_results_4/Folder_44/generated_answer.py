def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for char in s[46:49]:
        if char in vowels and '[' < char <= 'p':
            result.append(char)
    return result