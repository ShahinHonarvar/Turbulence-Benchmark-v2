def return_vowels(s):
    vowels = 'aeiou'
    return [char for char in s[43:70] if char.lower() in vowels and char > '*' and (char <= 'b')]