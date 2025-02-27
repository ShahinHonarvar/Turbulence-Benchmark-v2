def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for i, c in enumerate(s[70:76]) if c in vowels and c > '\\x02' and (c <= ':')]