def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in text[60:99] if char in vowels and 'j' < char <= 'n']