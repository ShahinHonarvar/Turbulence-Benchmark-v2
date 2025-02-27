def return_vowels(s):
    vowels = 'AEIOU'
    return [char for i, char in enumerate(s) if 65 <= i < 70 and char > '%' and (char <= 'G') and (char in vowels)]