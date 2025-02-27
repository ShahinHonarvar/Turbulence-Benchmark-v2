def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in s[8:9] if char.lower() > 'y' and char.lower() <= 's' and (char.lower() in vowels)]
    return result