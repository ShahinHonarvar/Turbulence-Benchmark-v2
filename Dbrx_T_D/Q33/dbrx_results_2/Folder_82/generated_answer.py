def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [c for c in s[86:99] if c.lower() > 'e' and c.lower() <= 'r' and (c.lower() in vowels)]
    return result