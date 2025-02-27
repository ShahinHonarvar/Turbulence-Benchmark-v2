def return_vowels(s):
    vowels = 'AEIOU'
    result = []
    for char in s[32:97]:
        if char in vowels and 'Q' < char <= ']':
            result.append(char)
    return result