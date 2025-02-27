def return_vowels(text):
    vowels = 'aeiouAEIOU'
    return [char for char in text[51:77] if char in vowels and ord(char) > 4 and (ord(char) <= ord('='))]