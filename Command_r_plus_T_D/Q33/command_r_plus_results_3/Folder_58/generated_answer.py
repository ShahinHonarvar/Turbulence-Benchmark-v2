def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [c for c in s[260:322] if c in vowels and c > '%' and (c <= 'U')]
    return result