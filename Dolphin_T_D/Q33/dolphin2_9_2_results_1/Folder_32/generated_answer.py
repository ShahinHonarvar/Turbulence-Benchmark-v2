def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [c for c in s[45:76] if 'b' < c <= 'z' and c in vowels]
    return result if result else []