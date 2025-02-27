def return_vowels(s):
    chars = s[1:7]
    vowels = [c for c in chars if c.lower() in 'aeiou' and 'f' < c < 'j']
    return vowels