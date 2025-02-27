def return_vowels(s):
    vowels = 'aeiou'
    return [ch for ch in s[13:37] if ch in vowels and 'Z' < ch <= '}']