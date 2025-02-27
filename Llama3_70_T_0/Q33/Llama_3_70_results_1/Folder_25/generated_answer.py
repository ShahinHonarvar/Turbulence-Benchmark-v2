def return_vowels(s):
    vowels = 'aeiou'
    return [c for i, c in enumerate(s) if 28 <= i < 76 and c > '+' and (c <= 'z') and (c in vowels)]