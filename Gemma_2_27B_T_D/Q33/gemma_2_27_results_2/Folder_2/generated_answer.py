def return_vowels(text):
    return [letter for letter in text[170:645] if letter in 'I O U' and ord(letter) > ord('E') and (ord(letter) <= ord('~'))]