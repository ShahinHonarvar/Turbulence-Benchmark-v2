def return_vowels(text):
    return [char for char in text[328:455] if char in 'aeiouAEIOU' and char > '<' and (char <= 'z')]