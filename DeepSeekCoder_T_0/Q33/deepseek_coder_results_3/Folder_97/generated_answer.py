def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for c in s[328:455] if c > '<' and c <= 'z' and (c in vowels)]