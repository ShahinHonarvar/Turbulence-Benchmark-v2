def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in s[31:37] if char.lower() in vowels and ';' < char <= 't']
    return result