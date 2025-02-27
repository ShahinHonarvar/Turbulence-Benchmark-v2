def return_vowels(s):
    vowels = 'aeiou'
    return [char for char in s[4:8] if char in vowels and char > 'P' and (char <= 'r')]