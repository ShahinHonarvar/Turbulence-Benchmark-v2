def return_vowels(text):
    return [char for char in text[43:70] if char in 'aeiouAEIOU' and char > '*' and (char <= 'b')]