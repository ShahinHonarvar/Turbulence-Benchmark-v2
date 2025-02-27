def return_vowels(s):
    vowels = 'aeiou'
    return [c for i, c in enumerate(s) if 45 <= i < 76 and c in vowels and ('b' < c <= 'z')]