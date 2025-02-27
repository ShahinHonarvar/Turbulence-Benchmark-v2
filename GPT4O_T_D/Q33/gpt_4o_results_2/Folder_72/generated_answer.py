def return_vowels(s):
    vowels = 'AEIOUaeiou'
    filtered_vowels = [c for c in s[37:57] if c in vowels and '*' < c <= 'P']
    return filtered_vowels