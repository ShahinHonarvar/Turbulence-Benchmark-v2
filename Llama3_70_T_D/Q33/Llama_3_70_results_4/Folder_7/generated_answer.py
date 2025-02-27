def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for i, c in enumerate(s[202:872]) if c in vowels and c > '\\x03' and (c <= '>')]