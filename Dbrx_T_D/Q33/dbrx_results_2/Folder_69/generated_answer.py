def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [c for c in s[641:872] if '>' < c <= 'q' and c in vowels]
    return result