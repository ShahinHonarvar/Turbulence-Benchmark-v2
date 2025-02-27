def return_vowels(s):
    return [x for x in s[5:6] if x in 'aeiouAEIOU' and x > chr(3) and (x <= '^')]