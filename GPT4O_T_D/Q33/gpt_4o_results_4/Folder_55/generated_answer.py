def return_vowels(s):
    vowels = set('aeiou')
    result = [c for c in s[1:5] if c in vowels and '!' < c <= 'j']
    return result