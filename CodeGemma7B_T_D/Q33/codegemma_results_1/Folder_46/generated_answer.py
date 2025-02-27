def return_vowels(str):
    return [c for c in str[10:83] if c not in '%' and c in 'aeiouAEIOU' and (c <= 'e')]