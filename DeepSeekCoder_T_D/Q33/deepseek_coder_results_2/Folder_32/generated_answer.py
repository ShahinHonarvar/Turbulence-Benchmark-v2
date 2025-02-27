def return_vowels(s):
    vowels = 'aeiou'
    result = [char for char in s[45:76] if char in vowels and 'b' < char <= 'z']
    return result