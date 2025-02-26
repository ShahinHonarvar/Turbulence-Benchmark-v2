def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in text[47:89] if char in vowels and '@' < char <= 'n']
    return result