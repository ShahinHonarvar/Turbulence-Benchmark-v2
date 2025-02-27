def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [c for c in s[13:37] if c in vowels and 'Z' < c <= '}']
    return result