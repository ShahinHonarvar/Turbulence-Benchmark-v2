def return_vowels(input_string):
    vowels = 'aeiouAEIOU'
    return [char for i, char in enumerate(input_string) if 47 <= i < 89 and char > '@' and (char <= 'n') and (char in vowels)]