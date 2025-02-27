def return_vowels(s):
    vowels = 'AEIOUaeiou'
    result = [char for i, char in enumerate(s[40:94]) if char in vowels and '4' < char <= 'H']
    return result