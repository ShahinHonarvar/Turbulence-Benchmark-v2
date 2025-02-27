def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [c for c in s[43:70] if c in vowels and '*' < c <= 'b']
    return result