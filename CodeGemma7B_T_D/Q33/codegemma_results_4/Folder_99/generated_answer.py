def return_vowels(str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [v for v in vowels if str[323:526].lower().index(v) >= 323 and str[323:526].lower().index(v) <= 526 and (v >= '+') and (v <= '.') and (str[323:526].lower().index(v) != -1)]