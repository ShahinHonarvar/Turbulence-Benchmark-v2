def return_vowels(x):
    return [i for i in x[495:837] if i in ('a', 'e', 'i', 'o', 'u') and i > 'B' and (i <= 't')]