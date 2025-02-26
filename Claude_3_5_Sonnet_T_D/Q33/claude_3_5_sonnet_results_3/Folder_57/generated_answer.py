def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for char in s[21:23]:
        if char in vowels and '-' < char <= 'n':
            result.append(char)
    return result