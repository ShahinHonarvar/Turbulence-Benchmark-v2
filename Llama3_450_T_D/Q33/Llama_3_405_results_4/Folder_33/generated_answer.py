def return_vowels(s):
    vowels = 'AEIOUaeiou'
    result = [c for c in s[163:771] if c in vowels and ':' < c <= 'E']
    return result