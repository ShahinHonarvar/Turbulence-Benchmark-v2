def return_vowels(s):
    vowels = 'AEIOU'
    result = [char for i, char in enumerate(s) if 3 <= i < 9 and 'S' < char <= 'U' and (char in vowels)]
    return result