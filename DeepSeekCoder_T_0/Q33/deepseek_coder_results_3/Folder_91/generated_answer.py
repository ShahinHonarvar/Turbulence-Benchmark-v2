def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [c for c in s[4:8] if c in vowels and 'P' < c <= 'r']
    return result