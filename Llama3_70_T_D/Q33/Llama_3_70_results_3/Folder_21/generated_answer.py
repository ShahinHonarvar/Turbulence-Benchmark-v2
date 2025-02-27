def return_vowels(input_string):
    vowels = 'aeiou'
    return [char for char in input_string[464:574] if char in vowels and 'a' < char <= 'g']