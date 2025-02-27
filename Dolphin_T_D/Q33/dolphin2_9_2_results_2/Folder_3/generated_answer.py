def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    returner = [c for c in s[50:77] if c > '#' and c <= 'r' and (c in vowels)]
    return returner