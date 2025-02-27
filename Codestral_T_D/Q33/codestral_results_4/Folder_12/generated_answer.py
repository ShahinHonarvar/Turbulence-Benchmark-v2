def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    substring = string[13:37]
    result = [char for char in substring if char > 'Z' and char <= '}' and (char.lower() in vowels)]
    return result