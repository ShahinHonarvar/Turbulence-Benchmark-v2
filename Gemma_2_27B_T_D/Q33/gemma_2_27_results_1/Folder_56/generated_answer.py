def return_vowels(text):
    return [char for char in text[15:86] if char in 'aeiouAEIOU' and ord(char) > ord('@') and (ord(char) <= ord('~'))]