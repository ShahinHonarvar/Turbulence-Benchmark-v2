def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in string[86:99] if char.lower() in vowels and 'E' < char.lower() <= 'r']
    return result