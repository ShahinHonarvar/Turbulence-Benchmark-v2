def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in s[64:82] if char.lower() in vowels and 'p' < char.lower() <= 'z']
    return result