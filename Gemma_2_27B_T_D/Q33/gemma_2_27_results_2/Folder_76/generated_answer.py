def return_vowels(text):
    return [char for char in text[495:837] if char in 'aeiouAEIOU' and char > 'B' and (char <= 't')]