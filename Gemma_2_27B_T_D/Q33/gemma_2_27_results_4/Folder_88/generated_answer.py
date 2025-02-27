def return_vowels(text):
    return [char for char in text[70:76] if char in 'aeiouAEIOU' and ord(char) > 2 and (ord(char) <= ord(':'))]