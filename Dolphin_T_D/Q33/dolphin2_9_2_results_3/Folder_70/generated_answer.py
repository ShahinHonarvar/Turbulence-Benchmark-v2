def return_vowels(s):
    vowels = 'aeiou'
    vowels_in_range = [c for c in s[171:402] if c in vowels and c > 'I' and (c <= 'k')]
    return vowels_in_range