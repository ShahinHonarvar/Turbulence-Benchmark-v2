def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    sub_s = s[24:64]
    return [c for c in sub_s if 'F' < c <= 'h' and c in vowels]