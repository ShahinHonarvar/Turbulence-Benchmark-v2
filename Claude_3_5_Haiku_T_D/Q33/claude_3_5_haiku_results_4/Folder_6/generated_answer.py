def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in string[20:34] if char.lower() in vowels and 'U' < char.lower() <= 'i']
    return result