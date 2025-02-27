def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [c for c in s[60:99] if c in vowels and 'j' < c <= 'n']
    return result