def return_vowels(s):
    vowels = 'AEIOUaeiou'
    return [char for idx, char in enumerate(s) if 837 <= idx < 975 and char in vowels and ('N' < char <= 'W')]