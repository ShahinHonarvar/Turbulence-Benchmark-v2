def return_vowels(string):
    return [char for char in string[323:526] if char in 'aeiouAEIOU' and char > '+' and (char <= ':')]