def return_vowels(s):
    vowels = 'aeiou'
    result = [char for i, char in enumerate(s[34:58]) if char in vowels and char > 'b' and (char <= 'o')]
    return result