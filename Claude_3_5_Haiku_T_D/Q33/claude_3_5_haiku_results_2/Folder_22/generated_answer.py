def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in string[56:90] if char.lower() in vowels and 'k' < char.lower() <= 'z']
    return result