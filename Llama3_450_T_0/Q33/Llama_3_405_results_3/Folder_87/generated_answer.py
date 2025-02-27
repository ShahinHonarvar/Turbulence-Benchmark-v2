def return_vowels(s):
    vowels = 'aeiou'
    result = [char for i, char in enumerate(s) if 34 <= i < 58 and 'b' < char <= 'o' and (char in vowels)]
    return result