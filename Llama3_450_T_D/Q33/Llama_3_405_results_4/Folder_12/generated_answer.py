def return_vowels(s):
    vowels = 'AEIOUaeiou'
    result = [c for i, c in enumerate(s) if 13 <= i < 37 and 'Z' < c <= '}' and (c in vowels)]
    return result