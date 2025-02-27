def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for c in s[1:9] if c in vowels and '?' < c <= 'k']