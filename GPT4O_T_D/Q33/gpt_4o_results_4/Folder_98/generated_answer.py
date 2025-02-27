def return_vowels(s):
    vowels = 'AEIOU'
    return [ch for ch in s[3:9] if ch in vowels and 'S' < ch <= 'U']