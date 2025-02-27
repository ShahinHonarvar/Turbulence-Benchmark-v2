def return_vowels(s):
    vowels = 'aeiou'
    return [char for char in s[71:81] if char in vowels and char > '>' and (char <= 'U')]