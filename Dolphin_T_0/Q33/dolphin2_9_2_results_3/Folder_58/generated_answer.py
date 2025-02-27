def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    sub = s[260:322]
    result = [c for c in sub if c > '%' and c <= 'U' and (c in vowels)]
    return result