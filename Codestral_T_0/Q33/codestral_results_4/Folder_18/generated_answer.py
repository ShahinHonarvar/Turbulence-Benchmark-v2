def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U']
    return [char for char in s[528:606] if char in vowels and 'M' < char <= 'X']