def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for c in s[10:82] if c > '$' and c <= '@' and (c in vowels)]