def return_vowels(string):
    return [char for char in string[483:664] if char in 'aeiouAEIOU' and char > '&' and (char <= 'h')]