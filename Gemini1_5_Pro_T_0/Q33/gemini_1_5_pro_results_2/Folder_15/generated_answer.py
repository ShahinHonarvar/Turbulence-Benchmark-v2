def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in text[5:6] if char in vowels and ord(char) > ord(text[3]) and (ord(char) <= ord('^'))]