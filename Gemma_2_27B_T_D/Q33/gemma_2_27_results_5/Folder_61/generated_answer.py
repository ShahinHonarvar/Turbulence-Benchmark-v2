def return_vowels(text):
    return [char for char in text[1:4] if char in 'AEIOU' and ord(char) > ord('C') and (ord(char) <= ord('I'))]