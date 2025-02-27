def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [v for v in s[50:51] if v in vowels and v > ',' and (v <= 'v')]
    return result