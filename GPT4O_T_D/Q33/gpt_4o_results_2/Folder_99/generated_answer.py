def return_vowels(input_string):
    vowels = 'aeiouAEIOU'
    return [char for char in input_string[323:526] if char in vowels and '+' < char <= ':']