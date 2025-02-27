def return_vowels(s):
    vowels = 'AEIOUaeiou'
    result = [char for i, char in enumerate(s[40:94]) if char in vowels and char > '4' and (char <= 'H')]
    return result