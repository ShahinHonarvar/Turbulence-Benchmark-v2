def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    return [c for c in s[71:88] if c in vowels and 9 < ord(c) <= ord('P')]