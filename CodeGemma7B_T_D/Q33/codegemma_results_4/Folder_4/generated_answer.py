def return_vowels(txt):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [l for l in txt[40:91] if l in vowels and ord(l) > ord('A') and (ord(l) <= ord('x'))]