def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in string[60:99] if char in vowels and 'j' < char <= 'n']
    return result