def return_vowels(s):
    vowels = 'aeiou'
    result = [c for c in s[1:9] if c in vowels and '?' < c <= 'k']
    return result