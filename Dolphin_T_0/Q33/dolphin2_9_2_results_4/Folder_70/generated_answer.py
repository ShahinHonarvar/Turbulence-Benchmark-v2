def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    return [c for c in s[171:402] if c in vowels and 'I' < c <= 'k']