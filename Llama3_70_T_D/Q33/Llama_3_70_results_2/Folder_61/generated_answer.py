def return_vowels(s):
    vowels = 'AEIOUaeiou'
    return [c for i, c in enumerate(s) if 1 <= i < 4 and c in vowels and ('C' < c <= 'I')]