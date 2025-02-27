def return_vowels(s):
    vowels = 'aeiou'
    result = [c for c in s[34:69] if c in vowels and '_' < c <= 'o']
    return result