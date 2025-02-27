def return_vowels(text):
    return [char for char in text[529:828] if char in 'vwxå¸®æ\x88\x91' and 'U' < char <= 'l']