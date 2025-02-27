def return_vowels(text):
    return [char for char in text[3:9] if char in 'EOIU' and 'S' < char <= 'U']