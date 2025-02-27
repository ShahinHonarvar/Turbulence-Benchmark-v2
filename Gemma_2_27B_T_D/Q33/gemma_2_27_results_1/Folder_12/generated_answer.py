def return_vowels(text):
    return [char for char in text[13:37] if char in 'aeiouAEIOU' and 'Z' < char <= '}']