def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [c for c in string[21:23] if c in vowels and '-' < c <= 'n']
    return result