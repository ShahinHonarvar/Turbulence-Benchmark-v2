def return_vowels(s):
    vowels = 'AEIOUaeiou'
    result = [c for i, c in enumerate(s) if 44 <= i < 95 and c in vowels and ('5' < c <= '<')]
    return result