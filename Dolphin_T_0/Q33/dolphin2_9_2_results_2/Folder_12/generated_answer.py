def return_vowels(s):
    vowels = 'aeiou'
    between_13_and_37 = s[13:37]
    filtered = [ch for ch in between_13_and_37 if 'Z' < ch <= '}' and ch in vowels]
    return filtered