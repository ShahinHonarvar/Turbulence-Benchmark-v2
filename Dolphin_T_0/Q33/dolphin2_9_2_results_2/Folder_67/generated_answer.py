def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    very_specific_range = s[21:59]
    specific_chars = [char for char in very_specific_range if char > '/' and char <= 'a']
    return [char for char in specific_chars if char in vowels]