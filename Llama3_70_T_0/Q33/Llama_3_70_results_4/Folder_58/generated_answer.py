def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for i, c in enumerate(s) if 260 <= i < 322 and c in vowels and ('%' < c <= 'U')]