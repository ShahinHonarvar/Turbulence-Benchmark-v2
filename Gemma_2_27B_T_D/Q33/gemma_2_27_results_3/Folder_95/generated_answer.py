def return_vowels(text):
    return [char for char in text[32:61] if char in 'aeiouAEIOU' and '?' < char <= 'P']