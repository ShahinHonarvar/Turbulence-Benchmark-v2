def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for i, c in enumerate(s) if 70 <= i < 76 and c in vowels and (c > '\\x02') and (c <= ':')]