def return_vowels(string):
    if len(string) < 276:
        return []
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in string[273:275] if char in vowels and '+' < char <= 'o']
    return result