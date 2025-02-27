def return_vowels(text):
    return [char for char in text[13:35] if char in 'aeiouAEIOU' and ord(char) > 8 and (ord(char) <= 70)]