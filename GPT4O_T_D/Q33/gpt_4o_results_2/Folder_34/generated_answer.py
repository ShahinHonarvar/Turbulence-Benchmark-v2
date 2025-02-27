def return_vowels(s):
    vowels = 'AEIOUaeiou'
    valid_chars = '1234567'
    return [ch for ch in s[19:32] if ch in vowels and ch in valid_chars]