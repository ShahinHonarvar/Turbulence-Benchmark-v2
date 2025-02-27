def return_vowels(text):
    return [char for char in text[71:88] if char in 'aeiouAEIOU' and chr(9) < char <= chr(80)]