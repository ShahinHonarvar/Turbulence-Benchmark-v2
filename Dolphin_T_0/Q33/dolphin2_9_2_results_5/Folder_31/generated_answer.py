def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [c for c in s if 65 <= ord(c) < 70 and c in vowels]
    return result