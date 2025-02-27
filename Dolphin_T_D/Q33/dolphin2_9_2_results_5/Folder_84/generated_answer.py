def return_vowels(text):
    vowels = 'aeiou'
    result = [c for c in text[770:852] if c in vowels and c > 'B' and (c <= 'i')]
    return result if result else []