def return_vowels(s):
    vowels = 'AEIOUaeiou'
    return [c for i, c in enumerate(s) if 528 <= i < 606 and c in vowels and ('M' < c <= 'X')]