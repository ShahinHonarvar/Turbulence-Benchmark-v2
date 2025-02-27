def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [s[i] for i in range(149, 313) if s[i] in vowels and s[i] > 'M' and (s[i] <= 'j')]