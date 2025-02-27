def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [c for c in s[1:5] if c in vowels and '!' < c <= 'j']
    return result