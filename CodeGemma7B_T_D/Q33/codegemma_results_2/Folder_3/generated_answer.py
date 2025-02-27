def return_vowels(str):
    vowels = list('aeiouAEIOU')
    return [x for x in vowels if x in str and str.index(x) >= 50 and (str.index(x) < 77) and (x > '#') and (x <= 'r')] or []