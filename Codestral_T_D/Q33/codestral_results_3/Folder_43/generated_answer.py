def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in string[22:82] if char in vowels and 'N' < char <= 'o']
    return result