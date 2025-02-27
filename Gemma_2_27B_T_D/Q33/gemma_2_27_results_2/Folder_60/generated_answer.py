def return_vowels(text):
    vowels = 'aeiouAEIOU'
    return [char for char in text[24:59] if char in vowels and char > 'N' and (char <= 'U')]