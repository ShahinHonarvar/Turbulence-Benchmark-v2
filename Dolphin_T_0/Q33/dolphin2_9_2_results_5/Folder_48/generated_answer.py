def return_vowels(s):
    vowels = 'aeiou'
    U, l = (ord('U'), ord('l'))
    result = [c for c in s[529:828] if U < ord(c) <= l and c in vowels]
    return result