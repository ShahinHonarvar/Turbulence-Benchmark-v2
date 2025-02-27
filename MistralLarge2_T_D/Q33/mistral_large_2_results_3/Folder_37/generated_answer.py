def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in string[82:90] if char.lower() in vowels and 'T' < char <= 'b']
    return result