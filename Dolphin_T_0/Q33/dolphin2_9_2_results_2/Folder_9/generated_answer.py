def return_vowels(text):
    vowels = 'aeiou'
    result = [c for c in text[13:35] if 'a' <= c <= 'f' and c in vowels]
    return result