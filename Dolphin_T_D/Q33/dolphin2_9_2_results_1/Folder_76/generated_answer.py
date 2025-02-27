def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in string[495:837] if char in vowels and char > 'B' and (char <= 't')]
    if len(result) == 0:
        return []
    else:
        return result