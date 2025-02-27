def return_vowels(s):
    vowels = 'aeiou'
    return [char for char in s[69:82] if char in vowels and '[' < char <= '~']