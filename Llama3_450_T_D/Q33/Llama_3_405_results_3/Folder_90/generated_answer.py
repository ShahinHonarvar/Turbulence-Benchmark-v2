def return_vowels(s):
    vowels = 'aeiou'
    result = [c for c in s[142:145] if c in vowels and '4' < c <= 'o']
    return result