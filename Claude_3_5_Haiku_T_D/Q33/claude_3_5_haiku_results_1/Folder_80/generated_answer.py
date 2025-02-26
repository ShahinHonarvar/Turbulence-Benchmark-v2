def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in text[85:99] if char in vowels and '/' < char <= 'n']
    return result