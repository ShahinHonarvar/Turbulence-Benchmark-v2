def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [s[i] for i in range(133, 306) if s[i] in vowels and s[i] > 'c' and (s[i] <= 'd')]