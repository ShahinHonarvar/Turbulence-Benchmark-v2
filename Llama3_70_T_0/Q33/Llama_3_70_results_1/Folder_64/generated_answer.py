def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for c in s[1:7] if c in vowels and 'F' < c <= 'j']