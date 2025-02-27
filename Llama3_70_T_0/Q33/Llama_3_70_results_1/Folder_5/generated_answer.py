def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for c in s[44:95] if c > chr(5) and c <= '<' and (c in vowels)]