def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in s[86:99] if char.lower() in vowels and 'E' < char <= 'r']
    return result