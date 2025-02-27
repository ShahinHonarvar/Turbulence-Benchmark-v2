def return_vowels(s):
    return [ch for ch in s[2:7] if ch in 'aeiou' and '^' < ch <= 'd']