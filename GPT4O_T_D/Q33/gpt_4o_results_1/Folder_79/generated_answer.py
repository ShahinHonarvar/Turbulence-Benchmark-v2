def return_vowels(s):
    vowels = 'AEIOU'
    result = []
    for char in s[74:96]:
        if char in vowels and 'I' < char <= 'X':
            result.append(char)
    return result