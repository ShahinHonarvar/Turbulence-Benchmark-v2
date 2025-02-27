def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [c for c in s[483:664] if c > '&' and c <= 'h' and (c in vowels)]
    return result