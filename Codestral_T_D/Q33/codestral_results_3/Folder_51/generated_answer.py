def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    substring = s[56:68]
    result = [char for char in substring if char in vowels and 'M' < char <= 'X']
    return result