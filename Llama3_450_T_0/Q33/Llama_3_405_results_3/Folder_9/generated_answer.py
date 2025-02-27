def return_vowels(s):
    vowels = 'AEIOUaeiou'
    result = [c for i, c in enumerate(s[13:35]) if c in vowels and '8' < c <= 'F']
    return result