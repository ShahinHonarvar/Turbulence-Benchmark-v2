def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    chars = s[273:275]
    result = [c for c in chars if c > '+' and c <= 'o' and (c in vowels)]
    return result