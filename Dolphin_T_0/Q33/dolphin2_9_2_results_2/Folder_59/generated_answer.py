def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    desired_chars = [char for char in s[8:9] if char > 'Y' and char <= 's']
    return [char for char in desired_chars if char in vowels]