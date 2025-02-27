def return_vowels(string):
    vowels = 'aeiou'
    return [c for c in string[1:5] if c in vowels and '!' < c <= 'j']