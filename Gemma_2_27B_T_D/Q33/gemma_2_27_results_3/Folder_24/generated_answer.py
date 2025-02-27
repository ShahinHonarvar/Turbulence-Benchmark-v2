def return_vowels(text):
    return [char for char in text[23:57] if char in 'aeiouAEIOU' and ord(char) > 0 and (ord(char) <= ord('d'))]