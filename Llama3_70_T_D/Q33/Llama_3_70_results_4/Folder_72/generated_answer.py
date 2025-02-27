def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [c for i, c in enumerate(s) if 37 <= i < 57 and c > '*' and (c <= 'P') and (c in vowels)]
    return result