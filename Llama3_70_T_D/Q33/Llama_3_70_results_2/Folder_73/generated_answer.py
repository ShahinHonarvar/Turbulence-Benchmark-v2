def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for i, c in enumerate(s) if 47 <= i < 89 and c > '@' and (c <= 'n') and (c in vowels)]