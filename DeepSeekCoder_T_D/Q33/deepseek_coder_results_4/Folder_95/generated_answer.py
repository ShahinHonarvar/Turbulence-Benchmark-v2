def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [c for c in s[32:61] if c > '?' and c <= 'P' and (c in vowels)]
    return result