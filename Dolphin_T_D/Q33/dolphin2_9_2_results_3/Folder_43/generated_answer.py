def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [v for v in s[22:82] if v in vowels and 'n' < v <= 'o']