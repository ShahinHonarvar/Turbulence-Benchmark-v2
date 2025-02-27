def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in text if char in vowels and ord(char) > ord('P') and (ord(char) <= ord('z'))]