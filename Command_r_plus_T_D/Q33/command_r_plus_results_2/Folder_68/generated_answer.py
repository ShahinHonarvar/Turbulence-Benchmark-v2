def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = [v for v in s[1:9] if v in vowels and v > '?' and (v <= 'k')]
    return result