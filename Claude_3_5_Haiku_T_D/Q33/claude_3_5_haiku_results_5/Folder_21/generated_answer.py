def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in string[464:574] if char in vowels and 'a' < char <= 'g']
    return result