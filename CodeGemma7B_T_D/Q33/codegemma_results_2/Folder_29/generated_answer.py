def return_vowels(txt):
    s = list(filter(lambda c: c in 'aeiouAEIOU' and 19 <= txt.index(c) < 20 and (c > '<') and (c <= 'p'), txt))
    return s or []