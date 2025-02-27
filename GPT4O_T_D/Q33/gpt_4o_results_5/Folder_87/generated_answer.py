def return_vowels(s):
    if len(s) < 35:
        return []
    vowels = 'aeiou'
    return [c for c in s[34:58] if c in vowels and 'b' < c <= 'o']