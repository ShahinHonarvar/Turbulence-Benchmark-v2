def return_vowels(string):
    return [char for char in string[50:51] if char in 'aeiouAEIOU' and char > ',' and (char <= 'v')]