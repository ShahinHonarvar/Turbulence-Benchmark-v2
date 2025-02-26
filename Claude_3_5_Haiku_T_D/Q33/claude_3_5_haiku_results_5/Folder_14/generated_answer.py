def return_vowels(text):
    vowels = 'aeiouAEIOU'
    result = [char for char in text[47:61] if char in vowels and '9' < char <= 'O']
    return result