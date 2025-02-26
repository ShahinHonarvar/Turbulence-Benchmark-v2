def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    return [char for char in string[3:9] if char in vowels and 'S' < char <= 'U']