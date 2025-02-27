def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [ch for ch in s[495:837] if ch in vowels and 'B' < ch <= 't']