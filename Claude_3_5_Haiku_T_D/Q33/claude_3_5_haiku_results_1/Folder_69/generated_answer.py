def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in string[641:872] if char in vowels and 'q' >= char > '>']
    return result