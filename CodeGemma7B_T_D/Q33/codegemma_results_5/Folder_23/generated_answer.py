def return_vowels(t):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    l = [a for a in t[56:96] if a in vowels and a > '&' and (a <= 'T')]
    if not l:
        return []
    return l