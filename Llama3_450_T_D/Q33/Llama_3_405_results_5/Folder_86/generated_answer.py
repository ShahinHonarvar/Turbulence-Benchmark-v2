def return_vowels(s):
    vowels = 'aeiou'
    result = [char for char in s[273:275] if char in vowels and '+' < char <= 'o']
    return result