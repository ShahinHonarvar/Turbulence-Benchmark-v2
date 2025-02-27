def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for i, c in enumerate(s) if 24 <= i < 68 and c in vowels and ('f' < c <= '|')]