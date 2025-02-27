def return_vowels(string):
    return [char for char in string[529:828] if char in 'VWeIo' and char > 'U' and (char <= 'l')]