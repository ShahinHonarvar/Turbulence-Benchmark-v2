def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for i, c in enumerate(s) if 12 <= i < 39 and c > ';' and (c <= '|') and (c in vowels)]