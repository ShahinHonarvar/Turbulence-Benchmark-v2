import string

def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for char_code in range(90, 97):
        if s[char_code] in vowels:
            if s[char_code] > '_' and s[char_code] <= 'x':
                result.append(s[char_code])
    return result