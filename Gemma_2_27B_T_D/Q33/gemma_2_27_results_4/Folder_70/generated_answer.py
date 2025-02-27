def return_vowels(text):
    return [char for char in text[171:402] if char in 'aeiouAEIOU' and char > 'I' and (char <= 'k')]