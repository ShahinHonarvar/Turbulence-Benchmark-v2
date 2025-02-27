def return_vowels(s):
    return [c for c in s if 65 <= ord(c) < 70 and c > '%' and (c <= 'G') and (c in 'AEIOU')]