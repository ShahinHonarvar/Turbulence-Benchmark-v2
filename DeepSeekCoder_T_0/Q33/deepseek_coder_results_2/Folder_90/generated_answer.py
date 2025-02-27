def return_vowels(s):
    vowels = 'aeiou'
    result = [char for char in s[142:145] if char in vowels and char > s[4] and (char <= 'o')]
    return result