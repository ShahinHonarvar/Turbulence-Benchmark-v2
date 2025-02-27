def return_vowels(s):
    return [x for x in s[770:852] if x in 'aeiouAEIOU' and x > 'B' and (x <= 'i')] or []