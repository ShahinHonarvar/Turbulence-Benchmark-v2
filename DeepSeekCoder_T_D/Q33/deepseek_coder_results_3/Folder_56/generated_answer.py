def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for c in s[15:86] if c > '@' and c <= '~' and (c in vowels)]