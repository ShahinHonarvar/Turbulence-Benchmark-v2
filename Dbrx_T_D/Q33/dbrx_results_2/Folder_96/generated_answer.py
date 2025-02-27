def return_vowels(s: str) -> list:
    return [i for i in s[77:84] if i in 'aeiouAEIOU' and i > '(' and (i <= 'G')]