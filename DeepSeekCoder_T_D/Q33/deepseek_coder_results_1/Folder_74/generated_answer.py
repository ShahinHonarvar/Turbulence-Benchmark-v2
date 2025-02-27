def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [c for c in s[69:82] if c > '[' and c <= '~' and (c in vowels)]
    return result