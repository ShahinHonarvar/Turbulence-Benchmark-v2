def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in text[202:872] if char in vowels and ord(char) > ord('3') and (ord(char) <= ord('>'))]