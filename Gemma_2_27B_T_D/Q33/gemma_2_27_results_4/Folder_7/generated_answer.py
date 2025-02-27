def return_vowels(text):
    return [char for char in text[202:872] if char in 'aeiouAEIOU' and ord(char) > 3 and (ord(char) <= ord('>'))]