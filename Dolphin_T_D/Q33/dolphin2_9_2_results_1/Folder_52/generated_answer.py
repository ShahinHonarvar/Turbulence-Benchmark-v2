def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [c for c in s[24:68] if c > 'f' and c <= '|' and (c in vowels)]
    return result