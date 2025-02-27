def return_vowels(s):
    vowels = 'aeiou'
    return [ch for ch in s[641:872] if ch > '>' and ch <= 'q' and (ch in vowels)]