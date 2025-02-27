def return_vowels(text):
    return [char for char in text[50:51] if char in 'aeiouAEIOU' and char > ',' and (char <= 'v')]