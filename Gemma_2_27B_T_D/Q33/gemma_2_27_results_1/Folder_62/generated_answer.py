def return_vowels(string):
    return [char for char in string[14:60] if char in 'EeIiOoUu' and char > 'D' and (char <= 'v')]