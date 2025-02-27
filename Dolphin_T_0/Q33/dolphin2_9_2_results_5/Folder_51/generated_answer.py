def return_vowels(s):
    vowels = 'aeiou'
    specified_range = s[56:68]
    return [c for c in specified_range if 'M' < c <= 'X' and c in vowels]