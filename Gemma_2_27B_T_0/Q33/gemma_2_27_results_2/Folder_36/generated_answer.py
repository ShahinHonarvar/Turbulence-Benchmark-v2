def return_vowels(string):
    return [char for char in string[604:949] if char in 'AEIOU' and char > 'N' and (char <= 'U')]