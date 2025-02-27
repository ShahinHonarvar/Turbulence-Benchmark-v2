def return_vowels(s):
    vowels = 'AEIOUaeiou'
    result = [char for i, char in enumerate(s[163:771]) if char in vowels and ':' < char <= 'E']
    return result