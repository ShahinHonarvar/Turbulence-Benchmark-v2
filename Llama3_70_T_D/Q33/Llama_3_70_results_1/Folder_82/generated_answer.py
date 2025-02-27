def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [c for c in s[86:99] if c in vowels and c > 'E' and (c <= 'r')]
    return result