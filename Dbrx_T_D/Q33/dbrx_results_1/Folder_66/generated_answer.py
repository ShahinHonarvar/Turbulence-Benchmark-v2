def return_vowels(string):
    vowels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
    result = [char for char in string[63:79] if char > 'D' and char <= 'y' and (char in vowels)]
    return result