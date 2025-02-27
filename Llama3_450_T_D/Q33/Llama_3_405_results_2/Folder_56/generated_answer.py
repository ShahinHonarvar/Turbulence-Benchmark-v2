def return_vowels(s):
    vowels = 'AEIOUaeiou'
    result = [c for i, c in enumerate(s) if 15 <= i < 86 and '@' < c <= '~' and (c in vowels)]
    return result