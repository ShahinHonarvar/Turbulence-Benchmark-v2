def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [ch for ch in s[47:89] if ch in vowels and '@' < ch <= 'n']