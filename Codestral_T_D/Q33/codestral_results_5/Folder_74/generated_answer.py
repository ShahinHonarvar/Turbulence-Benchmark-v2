def return_vowels(s):
    vowels = 'aeiou'
    return [ch for ch in s[69:82] if ch in vowels and '[' < ch <= '~']