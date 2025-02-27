def return_vowels(s):
    vowels = 'AEIOUaeiou'
    return [char for i, char in enumerate(s) if 13 <= i < 35 and char in vowels and ('8' < char <= 'F')]