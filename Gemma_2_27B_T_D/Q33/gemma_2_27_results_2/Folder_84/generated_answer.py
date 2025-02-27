def return_vowels(text):
    return [char for char in text[770:852] if char in 'eouia' and char > 'B' and (char <= 'i')]