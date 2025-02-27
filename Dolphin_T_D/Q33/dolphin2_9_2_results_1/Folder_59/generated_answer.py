def return_vowels(s):
    vowels = 'aeiou'
    result = [v for v in s[8:9] if v in vowels and v > 'Y' and (v <= 's')]
    return result