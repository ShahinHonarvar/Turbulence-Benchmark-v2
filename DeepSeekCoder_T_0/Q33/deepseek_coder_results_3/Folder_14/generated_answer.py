def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [c for c in s[47:61] if c in vowels and c > '9' and (c <= 'O')]
    return result