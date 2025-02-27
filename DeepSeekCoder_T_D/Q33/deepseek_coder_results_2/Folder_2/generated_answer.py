def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for c in s[170:645] if 'E' < c <= '~' and c in vowels]