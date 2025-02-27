def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for i, c in enumerate(s) if 69 <= i < 82 and '[' < c <= '~' and (c in vowels)]