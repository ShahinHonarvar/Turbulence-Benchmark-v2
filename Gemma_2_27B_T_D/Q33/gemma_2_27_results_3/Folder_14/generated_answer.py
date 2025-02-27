def return_vowels(string):
    return [char for char in string[47:61] if char > 9 and char <= ord('O') and (char in 'aeiouAEIOU')]