def return_vowels(text):
    return [char for char in text[64:82] if char > 'P' and char <= 'z' and (char in 'aeiouAEIOU')]