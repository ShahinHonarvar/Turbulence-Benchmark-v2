def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [c for c in s[56:96] if c in vowels and '&' < c <= 'T']
    return result