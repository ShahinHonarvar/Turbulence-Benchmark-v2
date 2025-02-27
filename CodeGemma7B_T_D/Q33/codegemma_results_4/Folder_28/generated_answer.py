def return_vowels(txt):
    vowels = list('AEIOU')
    vowels_in_range = vowels[40:50]
    result = [v for v in vowels_in_range if v > 'W' and v <= '[']
    return result if result else []