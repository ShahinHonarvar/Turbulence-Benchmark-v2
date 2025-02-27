def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [v for v in vowels if v > 'N' and v <= 'U' and (s.index(v) in range(24, 59))]
    return result or []