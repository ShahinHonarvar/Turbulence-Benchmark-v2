def return_vowels(s):
    vowels = 'aeiou'
    result = [char for i, char in enumerate(s) if 45 <= i < 76 and char > 'b' and (char <= 'z') and (char in vowels)]
    return result