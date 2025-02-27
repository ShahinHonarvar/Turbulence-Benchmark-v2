def return_vowels(s):
    lower_bound = max(s.index('?') + 1, 32)
    upper_bound = min(s.index('P'), 61)
    vowels = 'aeiou'
    return [char for char in s[lower_bound:upper_bound] if char.lower() in vowels]