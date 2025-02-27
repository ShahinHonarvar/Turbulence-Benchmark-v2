def return_vowels(s):
    return [v for v in s[13:37] if v > 'Z' and v <= '}' and (v.lower() in 'aeiou')]