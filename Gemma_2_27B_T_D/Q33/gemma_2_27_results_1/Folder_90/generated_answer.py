def return_vowels(text):
    return [char for char in text[142:145] if char in 'aeiouAEIOU' and ord(char) > ord('4') and (ord(char) <= ord('o'))]