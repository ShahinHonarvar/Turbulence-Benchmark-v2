def return_vowels(s):
    vowels = 'aeiou'
    result = [c for c in s[1:5] if '!' < c <= 'j' and c in vowels]
    return result