def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [v for v in s[64:82] if v > 'P' and v <= 'z' and (v in vowels)]