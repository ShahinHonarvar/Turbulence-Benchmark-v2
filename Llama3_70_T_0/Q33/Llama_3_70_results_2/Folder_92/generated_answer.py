def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for c in s[3:8] if c in vowels and ';' < c <= 'D']