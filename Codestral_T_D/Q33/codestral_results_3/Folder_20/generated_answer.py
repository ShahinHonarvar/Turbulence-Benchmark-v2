def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in string[59:61] if char in vowels and char > '+' and (char <= 'h')]