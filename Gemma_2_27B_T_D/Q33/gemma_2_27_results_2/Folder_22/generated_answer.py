def return_vowels(text):
    return [char for char in text[56:90] if char in 'aeiouAEIOU' and char > 'K' and (char <= 'z')]