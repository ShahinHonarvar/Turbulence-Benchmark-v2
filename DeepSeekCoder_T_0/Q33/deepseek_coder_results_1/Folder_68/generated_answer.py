def return_vowels(s):
    vowels = 'aeiou'
    result = [char for char in s[1:9] if char in vowels and '?' < char <= 'k']
    return result