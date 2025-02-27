def return_vowels(s):
    vowels = 'AEIOUaeiou'
    return [char for i, char in enumerate(s) if 163 <= i < 771 and char in vowels and (':' < char <= 'E')]