def return_vowels(s):
    vowels = set('AEIOU')
    return [ch for ch in s[74:96] if ch in vowels and 'I' < ch <= 'X']