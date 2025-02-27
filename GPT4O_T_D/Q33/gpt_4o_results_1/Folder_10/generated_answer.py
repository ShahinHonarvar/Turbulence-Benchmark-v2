def return_vowels(s):
    vowels = 'aeiouAEIOU'
    valid_chars = [c for c in s[31:37] if c in vowels and ';' < c <= 't']
    return valid_chars