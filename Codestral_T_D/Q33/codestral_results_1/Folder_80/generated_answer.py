def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in string[85:99] if char > '/' and char <= 'n' and (char in vowels)]