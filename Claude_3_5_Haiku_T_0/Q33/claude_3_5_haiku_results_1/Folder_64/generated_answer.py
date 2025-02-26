def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in string[1:7] if char.lower() in vowels and 'f' < char.lower() <= 'j']
    return result