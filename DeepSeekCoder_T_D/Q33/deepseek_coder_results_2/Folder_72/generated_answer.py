def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [c for c in s[37:57] if c in vowels and '*' < c <= 'P']
    return result