def return_vowels(s):
    vowels = 'aeiou'
    result = [ch for ch in s[22:82] if ch > 'n' and ch <= 'o' and (ch in vowels)]
    return result