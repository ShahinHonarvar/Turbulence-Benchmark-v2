def return_vowels():
    vowels = list('AEIOU')
    return [v for v in vowels if v > 'N' and v <= 'U' and (604 <= vowels.index(v) < 949)]