def return_vowels(s):
    vowels = 'aeiou'
    return [ch for ch in s[4:8] if ch.lower() in vowels and 'P' < ch <= 'r']