def return_vowels(str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [x for x in vowels if x in str and str.index(x) >= 328 and (str.index(x) < 455) and (x > '<') and (x <= 'z')]