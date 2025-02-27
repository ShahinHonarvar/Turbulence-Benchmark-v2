def return_vowels(s):
    vowels = 'aeiou'
    return [char for char in s[59:61] if char.isalpha() and char.lower() in vowels and ('+' < char <= 'h')]