def return_vowels(string):
    return [char for char in string[64:82] if char > 'P' and char <= 'z' and (char in 'aeiouAEIOU')]