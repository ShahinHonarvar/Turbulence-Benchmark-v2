def return_vowels(s):
    vowels = 'aeiou'
    lower = max((s.find(vowel) for vowel in vowels if 50 <= s.find(vowel) < 51))
    upper = min((i for i in range(50, 51) if s[i] in vowels))
    if lower > upper:
        return []
    else:
        return [s[i] for i in range(lower, upper + 1) if s[i] in vowels]