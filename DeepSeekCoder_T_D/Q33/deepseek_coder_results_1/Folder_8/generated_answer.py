def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [c for c in s[64:82] if c > 'P' and c <= 'z' and (c in vowels)]
    return result