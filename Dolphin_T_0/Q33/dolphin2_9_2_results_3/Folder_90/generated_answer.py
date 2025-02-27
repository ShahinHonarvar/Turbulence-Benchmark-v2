def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [s[i] for i in range(142, 145) if 4 < ord(s[i]) <= ord('o') and s[i] in vowels]