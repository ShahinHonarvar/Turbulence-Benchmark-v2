def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U']
    s_slice = s[3:8]
    result = [char for char in s_slice if 'A' < char <= 'D' and char in vowels]
    return result