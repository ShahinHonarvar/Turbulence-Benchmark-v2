def return_vowels(s):
    vowels = 'aeiou'
    valid_chars = 'klmn'
    return [char for char in s[60:99] if char in vowels and char in valid_chars]