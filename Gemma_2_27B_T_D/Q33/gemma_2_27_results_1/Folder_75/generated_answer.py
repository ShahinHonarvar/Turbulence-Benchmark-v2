def return_vowels(text):
    return [char for char in text[20:41] if char in 'aeiouAEIOU' and char > 'K' and (char <= 'Z')]