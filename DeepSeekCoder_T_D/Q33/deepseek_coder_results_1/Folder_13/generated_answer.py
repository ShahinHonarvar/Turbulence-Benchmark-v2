def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [c for c in s[149:313] if c in vowels and 'M' < c <= 'j']
    return result