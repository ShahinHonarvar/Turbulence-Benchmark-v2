def return_vowels(s):
    if len(s) < 9:
        return []
    vowels = 'aeiou'
    return [ch for ch in s[8:9] if ch in vowels and 'Y' < ch <= 's']