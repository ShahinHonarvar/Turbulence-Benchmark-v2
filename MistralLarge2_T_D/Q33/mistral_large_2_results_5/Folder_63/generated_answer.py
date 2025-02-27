def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for c in s[34:69] if c in vowels and '_' < c <= 'o']