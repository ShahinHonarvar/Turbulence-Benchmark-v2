def return_vowels(text):
    vowels = 'aeiouAEIOU'
    return [char for char in text[323:526] if char in vowels and '+' < char <= ':']