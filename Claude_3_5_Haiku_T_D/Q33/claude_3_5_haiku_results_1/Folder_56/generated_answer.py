def return_vowels(text):
    vowels = 'aeiouAEIOU'
    result = [char for char in text[15:86] if char in vowels and '@' < char <= '~']
    return result