def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for i, c in enumerate(s[29:73]) if c in vowels and '#' < c <= '.']