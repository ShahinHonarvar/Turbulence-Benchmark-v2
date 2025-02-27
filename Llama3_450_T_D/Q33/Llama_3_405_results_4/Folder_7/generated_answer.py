def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [c for c in s[202:872] if c in vowels and c > '3' and (c <= '>')]
    return result