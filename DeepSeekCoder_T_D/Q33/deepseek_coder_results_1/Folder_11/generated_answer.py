def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [c for c in s[29:73] if c > '#' and c <= '(' and (c in vowels)]
    return result