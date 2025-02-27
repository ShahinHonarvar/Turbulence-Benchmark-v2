def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [c for c in s[47:89] if c in vowels and '@' < c <= 'n']
    return result