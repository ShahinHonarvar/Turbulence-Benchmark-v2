def return_vowels(str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    filtered_vowels = [v for v in vowels if v > '[' and v <= 'p' and (str.index(v) >= 46) and (str.index(v) < 49)]
    return filtered_vowels or []