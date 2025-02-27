def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [c for c in s[69:82] if c >= '[' and c <= '~' and (c in vowels)]
    return result