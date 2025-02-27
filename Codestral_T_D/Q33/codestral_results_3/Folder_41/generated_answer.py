def return_vowels(s):
    vowels = 'aeiou'
    return [char for char in s[71:81] if char > '>' and char <= 'U' and (char in vowels)]