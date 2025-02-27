def return_vowels(s):
    vowels = 'aeiou'
    return [c for c in s[641:872] if c > '>' and c <= 'q' and (c in vowels)]