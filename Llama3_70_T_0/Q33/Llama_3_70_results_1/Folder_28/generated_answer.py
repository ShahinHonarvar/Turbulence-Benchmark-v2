def return_vowels(s):
    vowels = 'AEIOUaeiou'
    return [c for i, c in enumerate(s) if 41 <= i < 50 and c > 'W' and (c <= '[') and (c in vowels)]