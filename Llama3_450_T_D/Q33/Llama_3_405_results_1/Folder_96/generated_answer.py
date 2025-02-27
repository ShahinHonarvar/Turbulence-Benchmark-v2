def return_vowels(s):
    vowels = 'AEIOU'
    result = []
    for char in s[77:84]:
        if char > '(' and char <= 'G' and (char in vowels):
            result.append(char)
    return result