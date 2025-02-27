def return_vowels(string):
    return [char for char in string[528:606] if char in 'AEIOUYaeiouy' and char > 'M' and (char <= 'X')]