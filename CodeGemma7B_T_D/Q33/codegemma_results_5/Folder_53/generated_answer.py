def return_vowels(s):
    vowels = list('aeiouAEIOU')
    if 27 <= v[0] <= 57 and v > 'o' and (v <= 'w'):
        return [v for v in s if v in vowels and 27 <= v[0] <= 57 and (v > 'o') and (v <= 'w')]
    else:
        return []