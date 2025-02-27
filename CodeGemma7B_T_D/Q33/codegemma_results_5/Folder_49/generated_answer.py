def return_vowels(txt):
    return [x for x in txt[10:97] if x in {'a', 'e', 'i', 'o', 'u'} and x > 'R' and (x <= 'b')]