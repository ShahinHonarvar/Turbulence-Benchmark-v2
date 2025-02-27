def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    range_s = s[19:20]
    return [c for c in range_s if c in vowels and 'a' < c <= 'p']