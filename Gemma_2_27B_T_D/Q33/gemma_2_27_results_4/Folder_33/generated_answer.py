def return_vowels(s):
    return [c for c in s[163:771] if c in 'aeiouAEIOU' and c > ':' and (c <= 'E')]