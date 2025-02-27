def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for i, c in enumerate(s) if 328 <= i < 455 and c in vowels and ('<' < c <= 'z')]