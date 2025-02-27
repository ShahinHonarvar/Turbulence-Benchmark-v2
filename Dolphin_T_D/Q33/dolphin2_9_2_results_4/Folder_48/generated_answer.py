def return_vowels(s):
    vowels = ['U', 'u', 'O', 'o', 'I', 'i', 'A', 'a', 'E', 'e', 'l']
    return [ch for ch in s[529:828] if ch in vowels and ch > 'U' and (ch <= 'l')]