def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in string[163:771] if ':' < char <= 'E']
    result = [char for char in result if char in vowels]
    return result