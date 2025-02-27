def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [c for c in s[15:86] if '@' < c <= '~' and c in vowels]