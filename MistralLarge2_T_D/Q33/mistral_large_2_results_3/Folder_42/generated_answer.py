def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for c in s[12:39] if c in vowels and ';' < c <= '|']