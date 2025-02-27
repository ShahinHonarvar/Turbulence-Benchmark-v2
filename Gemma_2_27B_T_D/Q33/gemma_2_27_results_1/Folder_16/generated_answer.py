def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for c in s[133:306] if c in vowels and 'c' < c <= 'd']