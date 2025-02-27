def return_vowels(text):
    return [char for char in text[46:90] if char in 'aeiouAEIOU' and char > '@' and (char <= '[')]