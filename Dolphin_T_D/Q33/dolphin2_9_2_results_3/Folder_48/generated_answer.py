def return_vowels(s):
    vowels = 'aeiou'
    sub = s[529:828]
    return [c for c in sub if c > 'U' and c <= 'l' and (c in vowels)]