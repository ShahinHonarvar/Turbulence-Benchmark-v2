def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [c for c in s[202:872] if 3 < ord(c) <= ord('>') and c in vowels]
    return result