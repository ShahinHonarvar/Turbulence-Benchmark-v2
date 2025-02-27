def return_vowels(txt):
    return [i for i in txt[60:99] if i.lower() in 'aeiouAEIOU' and i > 'j' and (i <= 'n')] or []