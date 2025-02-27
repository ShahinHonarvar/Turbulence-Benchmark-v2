def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for c in s[641:872] if c in vowels and '>' < c <= 'q']