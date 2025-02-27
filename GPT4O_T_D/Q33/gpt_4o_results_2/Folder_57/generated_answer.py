def return_vowels(s):
    vowels = set('aeiou')
    return [ch for ch in s[21:23] if ch in vowels and '-' < ch <= 'n']