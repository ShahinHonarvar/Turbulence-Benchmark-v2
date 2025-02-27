def return_vowels(s):
    vowels = 'AEIOUaeiou'
    return [char for char in s[32:61] if char in vowels and '?' < char <= 'P']