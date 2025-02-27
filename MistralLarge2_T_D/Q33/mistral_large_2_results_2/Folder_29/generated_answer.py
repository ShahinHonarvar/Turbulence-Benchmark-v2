def return_vowels(text):
    vowels = 'aeiouAEIOU'
    result = [char for char in text[19:20] if char in vowels and '<' < char <= 'p']
    return result