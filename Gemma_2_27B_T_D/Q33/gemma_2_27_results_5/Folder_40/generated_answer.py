def return_vowels(s):
    return [x for x in s[2:7] if x in 'aeiouAEIOU' and x > '^' and (x <= 'd')]