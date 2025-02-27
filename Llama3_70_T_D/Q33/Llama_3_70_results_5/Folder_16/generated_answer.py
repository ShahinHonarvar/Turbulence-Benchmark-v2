def return_vowels(s, c, d):
    vowels = 'aeiouAEIOU'
    return [x for i, x in enumerate(s[133:307]) if x in vowels and c < x <= d]