def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [c for c in s[90:97] if c in vowels and '_' < c <= 'x']
    return result