def return_vowels(txt):
    return [x for x in txt[70:76] if x in 'aeiouAEIOU' and 2 < ord(x) <= ord(':')]