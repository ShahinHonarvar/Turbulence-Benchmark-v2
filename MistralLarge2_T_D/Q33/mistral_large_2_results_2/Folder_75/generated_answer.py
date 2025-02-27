def return_vowels(s):
    vowels = 'AEIOU'
    return [ch for ch in s[20:41] if ch in vowels and 'K' < ch <= 'Z']