def return_vowels(s):
    vowels = 'AEIOUaeiou'
    result = [c for c in s[13:35] if c > '8' and c <= 'F' and (c in vowels)]
    return result