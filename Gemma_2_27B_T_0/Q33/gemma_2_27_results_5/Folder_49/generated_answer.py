def return_vowels(s):
    return [c for c in s[10:97] if c in 'aeiouAEIOU' and c > 'R' and (c <= 'b')]