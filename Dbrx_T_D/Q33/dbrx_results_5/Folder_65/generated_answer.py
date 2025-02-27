def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U']
    result = [char for char in s[71:88] if char in vowels and '9' < char <= 'P']
    return result