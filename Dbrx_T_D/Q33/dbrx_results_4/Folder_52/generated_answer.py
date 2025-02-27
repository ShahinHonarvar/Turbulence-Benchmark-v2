def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in s[24:68] if char in vowels and 'f' < char <= '|']
    return result