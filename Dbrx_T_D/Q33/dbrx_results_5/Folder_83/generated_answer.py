def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [v for v in set(s[89:97]) if v in vowels and v > '_' and (v <= 'x')]