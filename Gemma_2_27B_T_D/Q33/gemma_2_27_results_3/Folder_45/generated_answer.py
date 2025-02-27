def return_vowels(text):
    vowels = 'aeiouAEIOU'
    return [char for char in text[43:70] if char in vowels and char > '*' and (char <= 'b')]