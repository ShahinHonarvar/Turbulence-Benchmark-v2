def return_vowels(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return [ch for ch in s[60:99] if ch in vowels and 'j' < ch <= 'n']