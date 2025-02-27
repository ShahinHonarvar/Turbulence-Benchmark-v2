def return_vowels(s):
    return [i for i in s if i in 'aeiouAEIOU' and 45 <= s.index(i) < 76 and (i > 'b') and (i <= 'z')] or []