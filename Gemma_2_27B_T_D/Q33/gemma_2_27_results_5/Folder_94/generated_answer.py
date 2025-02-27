def return_vowels(text):
    return [char for char in text[40:94] if char in 'aeiouAEIOU' and ord(char) > 4 and (ord(char) <= ord('H'))]