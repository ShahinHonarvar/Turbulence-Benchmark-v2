def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in string[64:82] if char.lower() in vowels and 'p' < char.lower() <= 'z']
    return result