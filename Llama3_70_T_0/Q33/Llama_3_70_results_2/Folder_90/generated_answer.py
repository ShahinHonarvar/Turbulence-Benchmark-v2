def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for c in s[142:145] if c in vowels and c > '4' and (c <= 'o')]