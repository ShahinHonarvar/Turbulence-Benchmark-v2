def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    chars = s[149:313]
    result = [c for c in chars if c > 'M' and c <= 'j']
    vowel_chars = [c for c in result if c in vowels]
    return vowel_chars