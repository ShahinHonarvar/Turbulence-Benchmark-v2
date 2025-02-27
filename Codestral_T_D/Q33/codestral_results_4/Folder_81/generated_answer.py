def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in string[20:43] if char in vowels and '5' < char <= 'm']