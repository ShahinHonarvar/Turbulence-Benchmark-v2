def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [ch for ch in s[22:82] if ch in vowels and 'n' < ch <= 'o']