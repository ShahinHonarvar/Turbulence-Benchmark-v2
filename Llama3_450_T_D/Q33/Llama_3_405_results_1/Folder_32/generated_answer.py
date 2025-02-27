def return_vowels(s):
    vowels = 'aeiou'
    result = [c for i, c in enumerate(s) if 45 <= i < 76 and 'b' < c <= 'z' and (c in vowels)]
    return result